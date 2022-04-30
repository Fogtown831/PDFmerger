#Merger all files
import os
from PyPDF2 import PdfFileMerger
source_dir=os.getcwd() #get current working directory

merger = PdfFileMerger()

for item in os.listdir(source_dir):
    if item.endswith('pdf'):
        merger.append(item)

merger.write("complete.pdf")
merger.close

#file merger
from PyPDF2 import PdfFileReader, PdfFileMerger
pdf_file1 = PdfFileReader("file1.pdf")
pdf_file2 = PdfFileReader("file2.pdf")
pdf_file3 = PdfFileReader("file3.pdf")
pdf_file4 = PdfFileReader("file4.pdf")
pdfoutput = PdfFileMerger()
pdfoutput.append(pdf_file1)
pdfoutput.append(pdf_file2)
pdfoutput.append(pdf_file3)
pdfoutput.append(pdf_file4)

with open("mergedfile.pdf", "wb") as finaloutput:
    pdfoutput.write(finaloutput)
