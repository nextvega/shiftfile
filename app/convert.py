import os
from django.conf import settings

# convertidor PDF > WORD
from pdf2docx import Converter
def convertPDF_to_word(pdf_file, name):
    documents_folder = os.path.join(settings.BASE_DIR, 'documents/docx')
    word_file = os.path.join(documents_folder, f'{name}.docx')
    cv = Converter(pdf_file)
    cv.convert(word_file, start=0, end=None)
    cv.close()
    
    return word_file

# convertidor TXT > PDF
from fpdf import FPDF
def convertTXT_to_pdf(txt_file, name):
    pdf_folder = os.path.join(settings.BASE_DIR, 'documents/pdf')
    pdf_file = os.path.join(pdf_folder, f'{name}.pdf')

    fichero = open(txt_file, "r")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=11)
    line = 1
    for linea in fichero:
        pdf.cell(200, 7, txt=linea, ln=line, align="L")
        if linea[-1] == ("\n"):
            linea = linea[:-1]
        line+=1

    pdf.output(pdf_file)

    return pdf_file