"""Write a program that will compute MPG for a car.
 Prompt the user to enter the number of miles driven and the number of gallons used.
 Print a nice message with the answer."""

mileage_B = int(input("Please enter your final mileage:"))
mileage_A = int(input("Please enter your beginning mileage:"))
gallons = int(input("Please enter the number of gallons used:"))

mileage = (mileage_B - mileage_A)
MPG = (mileage / gallons)

print("Your MPG is", MPG)