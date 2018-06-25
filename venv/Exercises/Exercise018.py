#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return thrice of their sum

n1=int(input("Enter number 1:"))
n2=int(input("Enter number 2:"))
n3=int(input("Enter number 3:"))

if (n1 == n2 and n2 == n3):
    answer=9*n1
    print("The 3 numbers are equal so, 3 times their sum is: ", answer)
else:
    answer=n1+n2+n3
    print("The sum of these 3 numbers is: ", answer)
