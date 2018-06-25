#Exercises from https://www.w3resource.com/python-exercises/python-basic-exercises.php
#Write a Python program which accepts a sequence of comma-separated numbers from user
# and generate a list and a tuple with those numbers

sampleData = input("Please enter number set as a comma separated list")
values = sampleData.split(",")
tuple = tuple(values)
print("values: ", values)
print("tuple: ", tuple)
