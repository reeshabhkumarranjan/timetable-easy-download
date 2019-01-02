# timetable-easy-download
A python script to download the latest timetable from my college's website.

NOTE: This project is under development and has bugs with the download service.
      For some reason, the download is not working.
      Stay tuned for fixes.

This script does the following things:
1. Deletes already existing timetable.pdf.
2. Downloads a new timetable.pdf.
3. Removes pages from timetable.pdf so that only a specific page is shown:
    Here, since I am in the CSE branch, I chose page number 5 (page number starts from 0), which shows me my timetable.
    Change the page number as per your stream.
4. Opens the timetable.pdf.
