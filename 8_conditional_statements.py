# Conditional Statements:-

    # These are used to get the output on the basis of condition

    # if  ==> only first condition
    # elif  ==> for rest of the conditions
    # else  ==> For Default condition

# Write a program to check the eligibilty for voting card

# age < 18   # Not Eligible
# age == 18  # Elgible
# age > 18   # Your are late.. Elgible

# age = int(input("Enter your age: "))

# if age > 0 and age < 18:
#     print("Not Elgible")
# elif age == 18:
#     print("Elgible")
# elif age > 18:
#     print("You are Late..! Eligible.")
# else:
#     print("Invalid Age") 


# ---------------------------

#  Write the program to find out weather user 
# entered number is even or odd

# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print("Even")
# else:
#     print("odd")


# ask user to enter his name.
# if name is less than 5 charecter ==> Small name
# if name is exactly 5 charecters ==> Good Name
# if name is more than 5 charecters == > Big Name

name = input("Enter your name: ")

if len(name) < 5:
    print("Small Name")
elif len(name) == 5:
    print("Good Name")
else:
    print("Big Name")
