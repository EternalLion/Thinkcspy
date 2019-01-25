"""Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).
Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours), and then ask for the number of hours to wait for the alarm.
Your program should output what the time will be on the clock when the alarm goes off.
"""


current_time_str = input("What is the current time (in hours)?")
waiting_time_str = input("How many hours would you like to wait for the alarm?")

current_time_int = int(current_time_str)
waiting_time_int = int(waiting_time_str)

hours = waiting_time_int + current_time_int

alarm = hours % 24

print("Your alarm will go off at", alarm, "hundred hours.")
