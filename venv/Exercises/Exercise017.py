#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#Write a Python program to test whether a number is within 100 of 1000 or 2000.

n=int(input("Enter a value"))
if(n<100):
    print(n," is less than 100")
elif(n<1000):
    print(n," is between 100 and 1000")
elif(n<2000):
    print(n," is between 1000 and 2000")
else:
    print(n," is over 2000")