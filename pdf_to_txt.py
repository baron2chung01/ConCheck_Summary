from scripts.pdf_to_txt import get_files,pdf_to_txt

# 1. convert contract pdf to txt
for filename in get_files("contract_pdf/"):
    # excluding post processed ocrmypdf
    if "ocrmypdf" not in filename:
        pdf_to_txt(filename)

# 2. get salary


