from pathlib import Path
from pypdf import PdfReader, PdfWriter

def read_pdf():

    pdf_path = (
            Path.home()
               /  "VSCode" /  "remove-lines-pdf" / "pdfs" / "questions.pdf")
    pdf_reader = PdfReader(pdf_path)
    for i in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[i]
        print(page)
        print(page.extract_text())
    


if __name__ == '__main__':
    read_pdf()