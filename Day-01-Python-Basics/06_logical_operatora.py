# Logical operators 
# Task_1 : Ask a user to enter there age(convert into integer) and  has_permission(y/n). 
# use and operator and check wether the person is 18 or older and has permission --- display result true or false 
# Task_2 : use or operator -- check whether the persons age is less than 18 or they do not have permission  display result
# Task_3 : use the not operator -- create boolean condition and use not to reverse its result.


# Task_1
age = int(input("Enter your age: "))
has_permission = input("Do you have permission? (y/n): ")

if has_permission == "y":
    has_permission = True
else:
    has_permission = False

result = age >= 18 and has_permission
print("Is the person 18 or older and has permission?", result)

# Task_2
result = age < 18 or not has_permission
print("Is the person less than 18 or does not have permission?", result)

# Task_3
condition = True
result = not condition
print("The negation of the condition is:", result)