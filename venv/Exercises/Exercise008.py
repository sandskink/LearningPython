#Exercises from https://www.w3resource.com/python-exercises/python-basic-exercises.php
#Write a Python program to display the first and last colors from the following list

colors=input("Enter colors in a comma-separated list")
colorList=colors.split(",")
print("The first color in that list is: " , colorList[0])
print("The last color in that list is: " , colorList[-1])
