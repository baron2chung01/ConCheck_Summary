import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span
import re
from scripts.preprocess import text_preprocess
from scripts.get_salary import filter


nlp = spacy.load("en_core_web_sm")
prep = text_preprocess("contract_txt/", "HA_AMT_FULL_TIME.txt")
text = prep.readFile()
doc = nlp(text)


regex = r"(?<!\S)((hkd|[$]|HKD|hk\$|HK\$) ?[\d,.]+[\d.,])(?!\S)"
pattern = [{"TEXT": {"REGEX": regex}}]


for sentence in doc.sents:
    filt = filter()
    x = filt.keyword_search(sentence.text)
    x = filt.stopword_filter(x)
    x = filt.salary_regex_search(x,regex)
    
    

    if x is not None:
        print("Sentence: " + sentence.text)
        print("Extracted: " + x.group(0))