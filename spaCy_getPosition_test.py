import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span
import re
from scripts.preprocess import text_preprocess
from scripts.get_postTitle import filter

def add_event_ent(matcher, doc, i, matches):
    # Get the current match and create tuple of entity label, start and end.
    # Append entity to the doc's entity. (Don't overwrite doc.ents!)
    match_id, start, end = matches[i]
    entity = Span(doc, start, end, label="EVENT")
    doc.ents += (entity,)
    print(entity.text)



nlp = spacy.load("en_core_web_sm")
prep = text_preprocess("contract_txt/", "HA_AMT_FULL_TIME.txt")
text = prep.readFile()
doc = nlp(text)






pattern = [{"TAG": {"REGEX": "^N"}}]


for sentence in doc.sents:
    matcher = Matcher(sentence.vocab)
    matcher.add("Post Title", [pattern], on_match=add_event_ent)
    filt = filter()
    x = filt.keyword_search(sentence.text)

    if x is not None:
        matches = matcher(sentence)    
