import PyPDF2
import sys
import os

merger = PyPDF2.PdfFileMerger()

for file in os.listdir(os.curdir) :
    if file.endswith(".pdf"):
        merger.append(file)
        #print(file)    #uncomment to check what files are going to be merged
    #Merge to new file name
    merger.write("Mod1Lecture.pdf")
