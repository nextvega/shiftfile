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


# convertidor IMG > PDF
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import portrait, landscape
def converterJPG_to_PDF(jpg_file, name, width, height):
    pdf_folder = os.path.join(settings.BASE_DIR, 'documents/pdf')
    pdf_file = os.path.join(pdf_folder, f'{name}.pdf')
    c = canvas.Canvas(pdf_file, pagesize=portrait)
    img = ImageReader(jpg_file)
    img_width, img_height = img.getSize()

    c.setPageSize((img_width, img_height))  # Establecer el tamaño de la página igual al tamaño de la imagen

    c.drawImage(img, 0, 0, width=img_width, height=img_height)
    c.save()

    return pdf_file


# compresor PDF
import fitz
def compress_to_pdf(pdf_converter, name):
    pdf_folder = os.path.join(settings.BASE_DIR, 'documents/pdf')
    pdf_file = os.path.join(pdf_folder, f'{name}.pdf')
    pdf_document = fitz.open(pdf_converter)
    pdf_document.save(pdf_file, garbage=255, deflate=True, clean=True)
    pdf_document.close()

    return pdf_file 