# type conversion
# task_1 : Create 2 variables :
    # a containing the string "10"
    # b containing the string "20"

a = "10"
b = "20"

# task_2 : print the result of a + b without converting their data types.
print("Results of a + b without converting them ", a + b)

# task_3 : Convert both variables into integers and print their sum.
print("Results of a + b after converting them into integer", int(a) + int(b))

# task_4 : Ask the user to eter two numbers.
num1= input("Enter number 1: ")
num2 = input("Enter number 2: ")

# Convert both inputs into integers and display their sum.
print("sum of both the numbers are :", int(num1) + int(num2))


# task_5 : Ask the user to enter their percentage as a decimal number.Convert the input into a floating-point value and print it.

percentage =input("Enter your percentage as a decimal number :")
print("percentage in a float ", float(percentage))