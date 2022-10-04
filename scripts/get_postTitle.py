import pandas as pd
import re
from nltk import tokenize
import os

class filter:

    def __init__(self):
        
        self.keyword_list = ['post title', 'position']
        self.stopword_list = []

    def keyword_search(self, sentence):
        if sentence is None: return None
        else:
            for word in self.keyword_list:
                if word in sentence.lower():
                    return sentence

            return None

    def stopword_filter(self,sentence):
        if sentence is None: return None
        else:
            cond = 1
            for i in list(range(len(self.stopword_list))):
                cond = cond * (self.stopword_list[i] not in sentence.lower())
            
            if cond == 1:
                return sentence
            else: return None
            #for word in self.stopword_list:
            #    if word not in sentence.lower():
             #       return sentence
            #return None

    def salary_regex_search(self,sentence,regex):
        if sentence is None: return None
        else:
            x = re.search(regex,sentence)
            if x is None: return None
            elif len(x.group(0)) > 1:
                    return x
            else: return None

    