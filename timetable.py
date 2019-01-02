import urllib.request
from PyPDF2 import PdfFileReader, PdfFileWriter
import os

url = "http://www.iiitd.ac.in/sites/default/files/docs/education/2019/Time%20Table-Add-Drop-Winter%202019V4.pdf"

if os.path.exists("timetable.pdf"):
    os.remove("timetable.pdf")

urllib.request.urlretrieve(url, "timetable.pdf")

pageNumberToExtract = 5
inputFile = PdfFileReader("timetable.pdf", "rb")
outputFile = PdfFileWriter()
pageToExtract = inputFile.getPage(pageNumberToExtract)
outputFile.addPage(pageToExtract)

with open("timetable2.pdf", "wb") as f:
    outputFile.write(f)

if os.path.exists("timetable.pdf"):
    os.remove("timetable.pdf")

os.rename("timetable2.pdf", "timetable.pdf")
