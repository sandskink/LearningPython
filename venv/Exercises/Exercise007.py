#Exercises from https://www.w3resource.com/python-exercises/python-basic-exercises.php
#Write a Python program to accept a filename from the user and print the extension of that

fileName = input("Enter a filename")
fileType = fileName.split(".")
print("This file is an ", fileType[-1])
