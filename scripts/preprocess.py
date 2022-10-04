from nltk import tokenize
import os

class text_preprocess:

    def __init__(self,input_folder,filename):
        self.input_folder = input_folder
        self.filename = filename

    def readFile(self):
        with open(self.input_folder + self.filename, 'r', encoding = 'UTF-8', errors="ignore") as file:
            x = file.read()
        
        # removing newlines & tabs
        x = x.replace("\n", " ")
        x = x.replace("\t", " ")

        return x