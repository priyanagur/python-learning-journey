# Ask the user to enter their marks out of 100.
# convert the input into integer.
# use if, elif, and  else to assign a grade according to these rules:
# 90-100 : A 
# 75-89 : B
# 60-74 : C
# 35-59 : D
# 0-34 : Fail
# below 0 or above 100 invalid marks 

# Display the approprate grade or invalid message

marks = int(input("Enter your marks out of 100 : "))

if marks < 0 or marks > 100:
    print("Invalid marks entered, enter correct marks out of 100")
elif marks >= 90:
    print("Grade : A")
elif marks >= 75:
    print("Grade : B")
elif marks >= 60:
    print("Grade : C")
elif marks >=35:
    print("Grade : D")
else :
    print("Fail")
    