#Exercises from https://www.w3resource.com/python-exercises/python-basic-exercises.php
#Write a Python program to print the calendar of a given month and year

import calendar
year=int(input("Enter the year you want to reference:"))
sMonth=input("Enter the month you want to reference as a number: ")
if(sMonth.isdigit()):
    month = int(sMonth)
    if (month<13 and month>0):
        print(calendar.month(year,month))
    else:
        print("Please enter a valid month")
else:
    print("please enter values as number")
