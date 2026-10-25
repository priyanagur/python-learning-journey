# Task-1 : Ask the user to enter a integer and convert it into a integer 
# use the modulus operator to check whether the number is even or odd. 
# display the appopirate message to the user.

number = int(input("Enter an integer : "))

if number % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

