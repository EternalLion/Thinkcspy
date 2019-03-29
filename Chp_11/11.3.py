"""Using the text file studentdata.txt (shown in exercise 1) write a program that calculates the minimum and maximum
score for each student. Print out their name as well."""

fileref = open("studentdata.txt", "r")
values = []

for aline in fileref:  # iterate through each line in the file
    values = aline.split()
    print('The grades for', values[0], 'are as follows: ', values[1:])
    scores = [int(i) for i in values[1:]]  # Convert strings in values list to int
    print('The minimum score for this student is: ', min(scores))
    print('The maximum score for this student is: ', max(scores))
    print('')  # Create a space to avoid wall of text

fileref.close()
