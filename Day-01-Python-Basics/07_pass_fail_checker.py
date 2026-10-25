# Ask user to enter there marks out of 100 
# convert the input into integer.
# use an if-else statement to check the marks.
# if the marks are 35 or above , display pass.
# if the marks are below 35, desplau fail 
# if the user enters marks greater than 100 or less then 0, display message indicating that the marks are invalid.

marks = int(input("Enter your exam marks out of 100 : "))

if marks < 0 or marks > 100:
    print("Invalid marks entered, please enter correct marks out of 100")
else :
    if marks >= 35:
        print("pass")
    else :
        print("fail")
