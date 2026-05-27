# Functions Practice:

    # No Argument Function

    # With Argument Function
        # positional argument function
        # Default argument function
        # keyword argument function
        # variable length argument function
        # variable length keyword argument function


# ----- No ARGUMENT FUNCTION

# Write a function which asks user to provide his/ her 
# age. on the basis of age tell user wether he/ she
# eligible for voting card.

# def eligibility_check_for_voting_card():
#     age = int(input("Enter your age: "))
#     if age < 18:
#         print("Not Eligible")
#     else:
#         print("Eligible")

# eligibility_check_for_voting_card()


#---- WITH POSITIONAL ARGUMENT FUNCTION:

# def eligibility_check_for_voting_card(age:int):
#     if age < 18:
#         print("Not Eligible")
#     else:
#         print("Eligible")

# eligibility_check_for_voting_card(23)
# eligibility_check_for_voting_card(12)


# ----- MULTIPLE POSITIONAL ARGUMENTS FUNCTION

# def eligibility_check_for_voting_card(firstname:str, lastname:str, gender: bool, age:int, citizenship:str):
#     if age < 18:
#         print(f"Not Eligible for Indian Voting Card {firstname} {lastname}.")

#     elif citizenship.lower() != "indian":
#         print(f"Not Eligible to get Indian Voting Card {firstname}  {lastname}.")

#     else:
#         print(f"Eligible to get Indian Voting Card {firstname} {lastname}.")
    # elif age >= 18 and citizenship.lower() != "indian":
    #     print(f"Not Eligible to get Indian Voting Card {firstname} {lastname}.")

    # elif citizenship.lower() == "indian" and age >= 18:
    #     print(f"Eligible to get Indian Voting Card {firstname} {lastname}.")


# eligibility_check_for_voting_card("Swapna", "Repala", False, 24, "Indian")

# eligibility_check_for_voting_card("Rushil", "Khatri", True, 25, "African")

#----------------------------------------------------

# ----------Variable Length Argument Functions

# Write a function to get the marks of students from class 10
# and print those marks which are above passing criteria of 
# the exam.

# def get_the_results(*args):
#     print("Your Results:")
#     for marks in args:
#         if marks < 40:
#             print(f"Fail: {marks}")
#         else:
#             print(f"Pass: {marks}")

# get_the_results(23, 56, 78, 10, 5, 99, 30, 50)


#----------- VARIABLE LENGTH KEYWORD ARGUMENTS FUNCTION

# Write a program where you take students name as a key and 
# its marks as value. print failed students list and 
# passed students list.

# def get_results(**kwargs):
#     failed = []
#     passed = []
#     for name, marks in kwargs.items():
#         if marks < 40:
#             # print(f"{name} Failed with {marks} marks")
#             failed.append(name)

#         else:
#             # print(f"{name} passed with {marks} marks")
#             passed.append(name)
#     print(f"Failed Students: {failed}")
#     print(f"Passed Students: {passed} ")


# students_marks = {"Swapna": 23, "Rushil": 67, "Raj": 45, "Hyndavi": 77, "Bhargav": 10}
# get_results(**students_marks)

#-------------------------------------

# Write a function to check wether user enetered 
# number is armstrong number or not 

# ------- 

# 153 ==> 1**3 + 5**3 + 3**3
    # ==> 1 + 125 + 27
    # ==> 153
# 1234 == 1 ** 4 + 2 ** 4 + 3 ** 4 + 4 ** 4

# def is_armstrong_number(num:int):  # 153
#     power = len(str(num))   # 3
#     total = 0  # 153
#     for digit in str(num):  # "153" "3"  3 ** 3  = 27
#         total += (int(digit) ** power)
#     if total == num:
#         print("Armstrong Number")
#     else:
#         print("No Armstrong Number")

# is_armstrong_number(345)
# is_armstrong_number(153)
# is_armstrong_number(5678)
# is_armstrong_number(1634)

#---------------------------
# Write a program to get the ascii numbers 
# of entered charecters

# def get_ascii_of_chars(*args):
#     for char in args:
#         print(f" {char} ==> {ord(char)}")

# get_ascii_of_chars("F", "*", "s", "9")

#----------------------------
# "A"  ==> 65 ==> 1000001

#----------------------------


# ----- HOMEWORK---------

# Factorial function  
# Write a function that calculates the factorial of a given number.

# Palindrome check  
# Write a function that checks if a given string is a palindrome.

# Prime number check  
# Write a function that checks if a given number is prime.

# frequency counter  
# Write a function that takes a string and returns a dictionary with word frequencies.

# List flattening  
# Write a function that flattens a nested list into a single list.
# Example:
    # l1 = [[1, 2, 3], [4, 5], 8, 7]
    # f_l1 = [1, 2, 3, 4, 5, 8, 7]


# Anagram checker  
# Write a function that checks if two strings are anagrams of each other.

# Matrix transpose  
# Write a function that transposes a given matrix (list of lists).

# Recursive sum of digits  
# Write a recursive function that sums the digits of a number until a single digit is obtained.