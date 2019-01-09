# timetable-easy-download
A python script to download the latest timetable from my college's website.

This script does the following things:
1. Deletes already existing timetable.pdf.
2. Downloads a new timetable.pdf.
3. Removes pages from timetable.pdf so that only a specific page is shown:
    Here, since I am in the CSE branch, I chose page number 5 (page number starts from 0), which shows me my timetable.
    Change the page number as per your stream.
4. Opens the timetable.pdf.

What you need to do:
1. Make sure you have Python 3 (and add it in system path).
2. In my batch file, I have used a ```python3 location\to\python\file```. You might have different PATH name for the Python 3 executable file. Please make sure you modify this particular line of the batch file.
3. Install pyPdf2 [```pip install pyPdf2```]
4. Change the address given in timetable.bat file.
5. Change the hardcoded values (url, addresses) if required.
6. Add the timetable.bat file in system path.

NOTE: The timetable will be created in the folder you open your cmd window to run ```timetable``` command.
