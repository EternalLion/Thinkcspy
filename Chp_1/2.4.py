"""It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday.
If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights.
Write a general version of the program which asks for the starting day number, and the length of your stay,
and it will tell you the number of day of the week you will return on."""

leave_day_str = input("Which day are you leaving (0 - 7)?")
length_of_stay_str = input("How many nights will you be away?")

leave_day_int = int(leave_day_str)
length_of_stay_int = int(length_of_stay_str)

vacation = leave_day_int + length_of_stay_int

vacation_length = vacation % 7

print(vacation_length)
