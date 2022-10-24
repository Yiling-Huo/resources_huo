# Automated processing of cloze task data in Chinese
# created by Yiling Huo, Oct 2022

# step 1: create an index file containing only common nouns from SUBTLEX-CH-WF_PoS

# requirement:
# SUBTLEX-CH-WF_PoS.xlsx, from SUBTLEX-CH.
# Cai Q, Brysbaert M (2010) SUBTLEX-CH: Chinese Word and Character Frequencies Based on Film Subtitles. PLoS ONE 5(6): e10729. https://doi.org/10.1371/journal.pone.0010729
# https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexch

import os, openpyxl, csv

inputFile = 'SUBTLEX-CH-WF_PoS.xlsx'
outputDir = (os.getcwd() + '/index/')
if not os.path.exists(outputDir):
    os.makedirs(outputDir)
print('Output file(s) are created in ' + outputDir)
print('Loading ' + inputFile + '...')

# read the xlsx file
xl = openpyxl.load_workbook(inputFile)
d = xl.active
data = []
for r in d.iter_rows(values_only=True):
    data.append(list(r))
print('Successfully loaded ' + inputFile)

# create an index file with only common nouns
with open(outputDir + 'index.csv', 'w', encoding = 'utf-8-sig') as outputfile:
    writer_to_file = csv.writer(outputfile, lineterminator = '\n') # the lineterminator parameter is needed in Windows
    first = True
    i = 0
    print('Extracting common noun...')
    for row in data:
        if first:
            first = False
            # skip the total word count row
            second = True
        elif second:
            # write down the headers, word form, pos, and pos frequency
            writer_to_file.writerow(row[2:])
            second = False
        elif row[0] == '@':
            # SUBTLEX-CH-WF_PoS has a summary row for every word, which stats with the word itself
            # and POS separete rows which begins with @. We only need the rows with beginning @.
            if row[3] == 'n': # common noun is marked using 'n' in SUBTLEX-CH
                writer_to_file.writerow(row[2:])
                i = i+1
                
print('Total number of common nouns: ' + str(i))
print('Done.')