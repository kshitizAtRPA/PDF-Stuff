import os
from PyPDF2 import PdfFileWriter, PdfFileReader


def rotate(pdf):
    if length:
        inputpdf = PdfFileReader(open(pdf, "rb"), strict=False)
        for i in range(inputpdf.numPages):
            file = PdfFileWriter()
            file.addPage(
                inputpdf.getPage(i).rotate_clockwise(
                    int(input("Enter rotation angle in clockwise: "))
                )
            )
            with open("%s-rotated.pdf" % (pdf.replace(".pdf", "")), "wb") as result:
                file.write(result)
    else:
        print("More than one pdf in the directory, exiting")
        exit


files = [f for f in os.listdir(".") if os.path.isfile(f) and f.endswith(".pdf")]
length = True
if len(files) > 1:
    length = False

pdf = str(files[0])
rotate(pdf)
