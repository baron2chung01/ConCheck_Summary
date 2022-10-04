import pandas as pd
import re
from nltk import tokenize
import os


def keyword_search(txt,keyword):
    if txt is None: return None
    else:
        for word in keyword:
            if word in txt:
                return txt

        return None

def stopword_filter(txt,stopword):
    if txt is None: return None
    else:
        for word in stopword:
            if word not in txt:
                return txt
        return None

def salary_regex_search(txt):
    if txt is None: return None
    else:
        x = re.search(r"(?<!\S)((hkd|[$]|HKD|hk\$|HK\$) ?[\d,.]+|[\d.,])(?!\S)",txt)
        if x is None: return None
        elif len(x.group(0)) > 1:
                return x
        else: return None


input_folder = "contract_txt/"
filename = "contract_sample.txt"

with open(input_folder + filename, 'r', encoding = 'UTF-8', errors="ignore") as file:
    # removing newlines & tabs
    txt = file.read()
txt = txt.replace("\n", " ")
txt = txt.replace("\t", " ")
txt_tokenize = tokenize.sent_tokenize(txt)

sentence_result = []
keyword = ['salary', 'wage']
stopword = ['allowance', 'renumeration']
for sentence in txt_tokenize:
    # filter keyword/stopword
    x = keyword_search(sentence, keyword)
    
    x = stopword_filter(x, stopword)
    
    x = salary_regex_search(x)
    
    # search for sentence with $ inside
    
    if x is not None:
        sentence_result.append(x.group(0))

print(sentence_result)




    

            