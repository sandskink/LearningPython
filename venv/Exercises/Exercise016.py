#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#  Write a Python program to get the difference between a given number and
# 17, if the number is greater than 17 return double the absolute difference

n=int(input("Enter a number: "))
difference=n-17
if(difference>0):
    print("The number entered is larger than 17, and 2 times the absolute difference is:")
    print(difference*2)