# If the file errors with "no module PyPDF2" then from command line, run pip install PyPDF2
import os
from os import listdir, mkdir, startfile
from os.path import isfile, join, exists
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

#Input file path and print the pdf files in that path
path = input("Enter the folder location: ")
pdffiles = [f for f in listdir(path) if isfile(join(path, f)) and '.pdf' in f]
print('\nList of PDF Files:\n')
for file in pdffiles:
    print(file)

# loops through pdffiles variable and adds blank page to end of each bill
def add_blank_to_end(pdffiles: list) -> list:
    names = []
    for f in pdffiles:
        pdf_in = open(path+'/'+f, 'rb')
        pdf_file = PdfFileReader(pdf_in)
        output = PdfFileWriter()
        output.appendPagesFromReader(pdf_file)
        totalpages = pdf_file.numPages
        if totalpages % 2 == 0:# if/else statement checks for even or odd pages in input PDF, if even, it skips adding blank page
            pass
        else:
            output.addBlankPage()
        names.append(f'b{f}')
        outputStream = open(f'b{f}', 'wb')
        output.write(outputStream)
    return names

#Input the name of the result file
resultFile = input("\nEnter the name of the result file : ")
if '.pdf' not in resultFile:
    resultFile += '.pdf'

#If the Output directory does not exist then create one
if not exists(path+'\\Output'):
    mkdir(path+'\\Output')

#Append the pdf files
merger = PdfFileMerger()
def merge_pdfs(pdffiles: list):
    #merger = PdfFileMerger()
    for f in pdffiles:
        merger.append(f)
    merger.write(path+'\\Output\\'+resultFile)

with_blank = add_blank_to_end(pdffiles)
merge_pdfs(with_blank)

# Close the merger process out of memory
merger.close()

# delete extra files
for i in with_blank:
    os.remove(i)

#Launch the result file
print('\n'+resultFile,'Successfully created!!! at ',path+'\\Output\\')
startfile(path+'\\Output\\'+resultFile)