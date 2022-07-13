import os
from PyPDF2 import PdfFileWriter, PdfFileReader


def split(pdf):
    if length:
        inputpdf = PdfFileReader(open(pdf, "rb"), strict=False)
        for i in range(inputpdf.numPages):
            file = PdfFileWriter()
            file.addPage(inputpdf.getPage(i))
            with open(
                "%s-page%s.pdf" % (pdf.replace(".pdf", ""), i + 1), "wb"
            ) as result:
                file.write(result)
    else:
        print("More than one pdf in the directory, exiting")
        exit


files = [f for f in os.listdir(".") if os.path.isfile(f) and f.endswith(".pdf")]
length = True
if len(files) > 1:
    length = False

pdf = str(files[0])
split(pdf)
