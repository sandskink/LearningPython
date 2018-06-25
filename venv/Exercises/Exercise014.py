#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#Write a Python program to calculate number of days between two dates
from datetime import date
sDateA=input("Enter date 1 (in format MM.DD.YYYY): ")
sDateB=input("Enter date 2 (in format MM.DD.YYYY): ")

lDateA=sDateA.split(".")
lDateB=sDateB.split(".")

iDateA=list(map(int,lDateA))
iDateB=list(map(int,lDateB))

dateA=date(iDateA[2],iDateA[0],iDateA[1])
dateB=date(iDateB[2],iDateB[0],iDateB[1])

difference=abs(dateA-dateB)
print("There are ",difference.days," between ",sDateA," and ",sDateB)