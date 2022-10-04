from scripts.get_salary import filter
from scripts.preprocess import text_preprocess
from nltk import tokenize

# text_preprocess
prep = text_preprocess("contract_txt/", "HA_AMT_FULL_TIME.txt")
text = prep.readFile()
text = tokenize.sent_tokenize(text)

# Generating summary table

# 1. get salary


sentence_result = []

for sentence in text:
    filt = filter()
    # filter keyword/stopword
    x = filt.keyword_search(sentence)
    
    x = filt.stopword_filter(x)
    
    x = filt.salary_regex_search(x)
    
    # search for sentence with $ inside
    
    if x is not None:
        sentence_result.append(x.group(0))

print(sentence_result)

