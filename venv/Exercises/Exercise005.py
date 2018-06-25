#Exercises from https://www.w3resource.com/python-exercises/python-basic-exercises.php
#Write a Python program which accepts the user's first and last name and print them in reverse order with
# a space between them

fullName = input("Please enter your full name (First Last)")
nameBreak = fullName.rfind(" ")
nameParts = fullName.split(" ")
numNames = len(nameParts)
if numNames == 2 :
    print(nameParts[1] + ", " + nameParts[0])
else:
    print("Name was entered incorrectly")

