Automated processing of Chinese cloze task data

Pre-requisites:

- These scripts require SUBTLEC-CH-WF_PoS, created by Cai, Q., & Brysbaert, M. (2010). SUBTLEX-CH: Chinese Word and Character Frequencies Based on Film Subtitles. Plos ONE, 5(6), e10729. https://doi.org/10.1371/journal.pone.0010729.
SUBTLEX-CH is available at https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexch.

- Have the scripts, SUBTLEX-CH, and cloze data (one csv file) in the same directory.

Step 1:

Run 01_create_index_using_SUBTLEX_CH_PoS.py. This creates an index files containing all common nouns from SUBTLEX-CH.

Step 2:

Run 02_process_cloze_data.py. Change the value of inputFile if needed. This script matches the common nouns with the cloze data, outputs a csv file indicating frequency and cloze probability of all common nouns occurred in responses.
