import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span
import re
from scripts.preprocess import text_preprocess
from scripts.get_salary import filter


nlp = spacy.load("en_core_web_sm")
prep = text_preprocess("contract_txt/", "CTF_Employment contract.txt")
text = prep.readFile()
doc = nlp(text)


for sentence in doc.sents:
    print(sentence.text)
    print('-'*20)