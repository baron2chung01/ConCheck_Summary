import pytesseract
from pdf2image import convert_from_path
import glob
from unittest import result
from tika import parser
import pandas as pd
import os
import pdfplumber

def get_files(path): # get all filenames in a folder

    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

def pdf_to_txt(filename,input_folder = "contract_pdf/", output_folder = "contract_txt/"):

    input_path = input_folder + filename
    output_path = output_folder + filename[:-4] +'.txt'

    pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\BC\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'

    results = parser.from_file(input_path)
    if results["content"] is None: # pdf does not have OCR layer

        # adding OCR layer to the pdf
        os.system(f'ocrmypdf {input_path} {input_path[:-4]}_ocrmypdf.pdf')

        # extract text from pdf using OCR
        with pdfplumber.open(f'{input_path[:-4]}_ocrmypdf.pdf') as pdf:
            for index,page in enumerate(pdf.pages):
                text = page.extract_text(x_tolerance=2)
                if index == 0: # truncate existing txt
                    with open(output_path, 'w') as f:
                        f.write(text+'\n')
                else:
                    with open(output_path, 'a') as f: # continue writing next page on same txt
                        f.write(text+'\n')


    else: # pdf has OCR layer, directly extract to txt
        content = results["content"].strip()
        with open(output_path, 'w', encoding = 'UTF-8') as f:
                f.write(content)