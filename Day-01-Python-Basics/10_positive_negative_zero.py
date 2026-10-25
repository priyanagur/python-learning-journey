# Task : Ask the user to enter an integer and convert it into an integer.
# use if,elif, and else to check the number :
         # if the number is greater then 0, display positive 
         # if the number is less then 0, display negative.
         # if the number is equals 0, display zero.

num = int(input("Enter a number"))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
elif num == 0:
    print("number is Zero")
else:
    print("Invalid")

