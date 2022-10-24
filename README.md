# Resources

Scripts and resorces that I have created or modified. 

**Praat_scripts:**
  - Add_silence_using_textgrids:
    a praat script that adds silence between each uniquely named textgrid interval according to the stimuli onset asynchrony. If dealing with speech stimuli, there is also an option to add punctuation.
  - Extract_pitch_contour:
    a praat script that extracts pitch contours using sound files and textgrid files. For each textgrid interval with a name, get pitch info  at 0% to 100% (by 10%) time. Outputs csv.

**Python_scripts:**
***Automated_processing_of_Chinese_cloze_responses:***
  Two scripts that process data collected from cloze tasks in Chinese. In a cloze task, the participant sees incomplete sentences and is asked to complete the sentence by providing one or a few words.
  - 01_create_index_using_SUBTLEX_CH_PoS.py:
    creates an index file containing all words that are parsed as 'common noun' in the SUBTLEX-CH-WF-PoS corpus. The SUBTLEX-CH corpus is created by Cai and Brysbaert (2010).
    requires SUBTLEX-CH-WF_PoS.xlsx. Available at https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexch
    References: Cai, Q., & Brysbaert, M. (2010). SUBTLEX-CH: Chinese Word and Character Frequencies Based on Film Subtitles. *Plos ONE*, 5(6), e10729. https://doi.org/10.1371/journal.pone.0010729
   - 02_process_cloze_data.py:
    count all occurrence of common nouns in the response. Requires a csv data file containing sentences and responses. Outputs a csv file (defult utf-8-bom) that contains sentence, response, count, cloze probability, and number of response.
