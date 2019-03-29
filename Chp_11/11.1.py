"""The following sample file called studentdata.txt contains one line for each student in an imaginary class.
The student’s name is the first thing on each line, followed by some exam scores.
The number of scores might be different for each student.

SAMPLE:
joe 10 15 20 30 40
bill 23 16 19 22
sue 8 22 17 14 32 17 24 21 2 9 11 17
grace 12 28 21 45 26 10
john 14 32 25 16 89

Use studentdata.txt to write a program that prints out the names of students that have more than six quiz scores."""

fileref = open("studentdata.txt", "r")

for aline in fileref: #iterate through each line in the file
        values = aline.split()
        if values[7:]: #if more than 6 grades exist
            print(values[0], values[7:]) #print the name and grades

fileref.close()