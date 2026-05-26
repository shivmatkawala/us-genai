# Functions:--->
    # Functional Programming Pardigm:
        # write a function but it will not excute until
        # it is called.

        # Reusibility of code increased.


# How to create a function:
    # Head of function  # starts with def function_name():
    # Body of function  #  same procedural code

# write a program to print all even numbers in between 
# 20 to 50.
# def evens():
#     for i in range(20, 50):
#         if i % 2 == 0:
#             print(i)

# write a program to to greet
# def greet():
#     print("Hello World")

# write a program to reverse a list
# def reverse_list():
#     l1 = [1, 2, 3, 4, 5, 6]
#     print(l1[::-1])


# evens()

# greet()
# greet()

#-------------------------------------

# Write a function to print all numbers which are divisible by 
# 13 in between 1 and 100

# def nums_divisible_by_13():
#     for i in range(1, 100):
#         if i % 13 == 0:
#             print(i)

# nums_divisible_by_13()


# return ==> it has the answer but never prints ==> production
# print  ==> it gets the answer and prints  ==> debugging

#----------------------------------------

# Write a program to get all vowels from a word 
# called "HAKUNAMATATA"

# def vowels():
#     for i in "HAKUNAMATATA":
#         if i.lower() in "aeiou":
#             print(i)

# vowels()

#---------------------------------------

# Write a program to get the odd numbers which are divisible 
# by 7 in between 1 and 100

# def divisible_by_7():
#     for i in range(1, 100):
#         if i % 2 != 0 and i % 7 == 0:
#             print(i)

# divisible_by_7()

# --------------------------------------
# Write a function to print addition of
# 5 and 7

# def addition():
#     print(5 + 7)

# addition()


#----------------------------------
# Functions Types:-
    # no argument function
        # Function which takes no argument (input parameter)
# def greet():
#     print("Hello Buddy..!")

# greet()

    # with argument function:
        # postional arguments function
# def greet(name:int):
#     print(f"Hello {name}")

# greet("Bhargav")
# greet("Swapna")
# greet("Rushil")
# greet(23)

#-------------------------
# def addition(num1, num2):
#     print(num1+num2)

# addition(2, 2)
# addition("Hyndavi", "Python")

# def my_info(name, age, gender):
#     print(f"My name is {name}\nMy age is {age}\nMy Gender is {gender}")

# my_info("Shiv", 33, "Male")
# my_info("Male", "Kiran", 55)

# color = "Pink"
# print(f"I like {color}")


        # default arguments function
# def greet(name="Buddy"):
#     print(f"Hello {name}")

# greet()
# greet("Swapna")

        # keyword argument fucntion
# def employee_info(eid, firstname, lastname, email, salary):
#     print(f"Employee Details:\nEID: {eid}\nFIRSTNAME: {firstname}\nLASTNAME: {lastname}\nSALARY: {salary}\nEMAIL: {email}")

# employee_info(email="sm@gmail.com", firstname='Shivakumar', lastname="Matkawala", salary=34000, eid=101)


        # variable length arguments fucntion
# Write a function to perform addition
# def addtion(*args):
#     total = 0
#     for i in args:
#         total+=i
#     return total

# addtion(2, 5, 7, 8)

        # variable length keyword argument function
            # key must be a string
# def xyz(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)

# xyz(**{"A": 65, "B": 66, "C": 67, "D": 68})
# xyz(Apple="Fruit", Hammer="Tool")
# xyz(one='1', two='4')