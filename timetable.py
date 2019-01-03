import urllib.request
from PyPDF2 import PdfFileReader, PdfFileWriter
import os
import ctypes


def run():
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

    ctypes.windll.user32.MessageBoxW(
        0, "Succesfully fetched the latest timetable for CSE 2nd Year! Click \"OK\" to continue", "Success", 0)


if __name__ == "__main__":
    try:
        run()
    except PermissionError as pe:
        ctypes.windll.user32.MessageBoxW(
            0, "The file is open in some other program. Click OK to continue", "Error", 0)
