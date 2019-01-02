"""Write a function which is given an exam mark, and it returns a string — the grade for that mark.

Mark	Grade
>= 90	A
[80-90)	B
[70-80)	C
[60-70)	D
< 60	F

The square and round brackets denote closed and open intervals.
A closed interval includes the number, and open interval excludes it. So 79.99999 gets grade C , but 80 gets grade B.

Test your function by printing the mark and the grade for a number of different marks."""


def getGrade():
    mark = float(input("Please enter the mark: "))

    if mark >= 90:
        print(f"The mark {mark} gets the grade A")
        print("{}, A".format(mark))
    elif mark >= 80:
        print(f"The mark {mark} gets the grade B")
    elif mark >= 70:
        print(f"The mark {mark} gets the grade C")
    elif mark >= 60:
        print(f"The mark {mark} gets the grade D")
    else:
        print(f"The mark {mark} gets the grade F")


getGrade()
