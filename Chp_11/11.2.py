"""Using the text file studentdata.txt (shown in exercise 1) write a program that calculates the average grade for each
student and print out the student’s name along with their average grade."""

fileref = open("studentdata.txt", "r")
values = []

from statistics import mean

for aline in fileref: #iterate through each line in the file
    values = aline.split()
    print('The grades for', values[0], 'are as follows: ', values[1:])
    scores = [int(i) for i in values[1:]] #Convert strings in values list to int
    print('The average score for this student is: ', mean(scores))
    print('') #Create a space to avoid wall of text
    
fileref.close()

