# Automated processing of cloze task data in Chinese
# created by Yiling Huo, Oct 2022

# step 2: cloze task data processing

# logic:
# 1. count all occurrence of common nouns in the response
# 2. to avoid multiple counting, if a match is completely contained in another match, only count the longest match
#    for example, if the response is 烤鸭, we only count 烤鸭, not both 烤鸭 and 鸭.

# requirement:
# 1. index.csv in /index/, created by 01_create_index_using_SUBTLEX_CH_PoS.py
# 2. a csv file containing cloze task data, default encoding utf-8.
#    the data file should at least contain two columns:
#         sentence column: indicating the sentence frame (what participants see during the task)
#         response column: participants' response

# note: if there is no match between the common nouns and the response, the script will output 'no_match'.
#       if there are many 'no_match's for a sentence, it's possible that the highest cloze probability answer is not included in SUBTLEX-CH's common noun corpus.

import os, csv

# settings
inputFile = 'data.csv'
outputFile = 'cloze_results.csv'
responseColumn = 'response' # the column name of responses
sentenceColumn = 'sentence' # column name of sentence frame

outputFormat = 'utf-8-sig' # output format. Default outputs a utf-8 csv file with BOM to read easily in MS Excel

header = ['sentence', 'response', 'count', 'cloze_probability', 'number_of_response'] # header of the output file


# create the index list. This is a list that contains all common nouns (pos: n) from SUBTLX-CH
print('Creating common noun index...')
with open(os.getcwd() + '/index/index.csv', 'r', encoding = 'utf-8') as ind:
    readind = csv.reader(ind)
    indexall = [line[0] for line in readind]
    index = indexall[1:]
    # sort the list by length then alphabet, longest to shortest
    # such that the first match in the loops below will be the longest word
    index.sort(key=lambda x: (len(x),x), reverse=True)
    print('Common noun index created.')

# process cloze data
print('Processing cloze data...')
# load data
with open(inputFile, 'r', encoding = 'utf-8') as fin:
    cr = csv.reader(fin)
    filecontents = [line for line in cr]
    print('Data loaded.')
    # create a list of unique sentences for the loops
    print('Creating sentence list...')
    first = True
    sentence = []
    for line in filecontents:
        if first:
            sentenceIndex = line.index(sentenceColumn)
            responseIndex = line.index(responseColumn)
            first = False
        else:
            sentence.append(line[sentenceIndex])
    sentenceuni = set(sentence)
    sentenceunique = list(sentenceuni)
    print('Sentence list created.')


    with open(outputFile, 'w', encoding = outputFormat) as out:
        writer_to_file = csv.writer(out, lineterminator = '\n')
        # write the header row
        writer_to_file.writerow(header)
        print('Output file created.')
        print('Looping through sentences...')
        sennum = 0
        for sen in sentenceunique:
            sennum = sennum+1
            # create a list of all responses
            responses = []
            numeral = []
            n = 0 # for counting how many responses
            for row in filecontents:
                if row[sentenceIndex] == sen:
                    responses.append(row[responseIndex]) # add to the response list
                    n = n+1 # count the response
                            
            # match response with index noun
            result = []
            for i in range(len(responses)):
                matches = []
                for j in index:
                    if j in responses[i]:
                        # only append j if j is a new unique item
                        # e.g. don't append 鸭 if 烤鸭 is already in the matches
                        if all(x in ''.join(matches) for x in [j]):
                            pass
                        else:
                            matches.append(j)
                if len(matches) == 0:
                    matches.append('no_match')
                result = result + matches
                
            # count frequency and calculate cloze probability of each item in result
            con = []
            for i in result:
                num = [i, result.count(i), result.count(i)/n]
                if num not in con:
                    con.append(num)
                    
            # write results to output file
            for i in range(len(con)):
                out_row = []
                out_row.append(sen) # sentence frame
                out_row = out_row + con[i] # answer, count, cloze probability
                out_row.append(n)  # number of response
                writer_to_file.writerow(out_row)

print('Done.')
