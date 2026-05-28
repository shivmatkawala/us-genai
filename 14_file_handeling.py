# File Handeling:-

        # Creating,
        # Reading,
        # Writing,
        # appending,
        # managing files using python built in functions.

# open()  ==> The core function in python for file handling.

# open(filename, mode)
    # filename :-  name of a file.
    # mode:- 
            # "r"  ==> Read file
            # "w"  ==> Write (overwrite)
            # "a"  ==> append 
            # "r+" ==> Read + Write   

#-----------Practical

# ==============read the entire file:

# file = open("sample.txt", "r")
# content = file.read()
# print(content)

# ================Read line by line

# file = open("sample.txt", "r")

# for line in file:
#     print(line.strip())

# file.close()

# ==================Writing to a file.

# file = open("sample.txt", "w")
# file.write("Welcome to python\n")
# file.write("File Handeling Example")

# =============Appending to a file

# file = open("sample.txt", "a")
# file.write("\nNew Line added")

#---------------------------------
# Using "with" statement (Best Practice)

# Reading:

# with open("sample.txt", "r") as file:   # file = open("sample.txt", "r")
#     content = file.read()
#     print(content)

# Writing:

# with open("wonderwomen.txt", "w") as file:
#     file.write("This is Marvel charecter.")


#--------------- Read single line

# with open("wonderwomen.txt", "r") as file:
#     print(file.readline())

#--------------- Read list of lines

# with open("wonderwomen.txt", "r") as file:
#     list_of_lines = file.readlines()

# print(list_of_lines[4])


#----------------------------- OS MODULE
import os

# check if file exists.

# if os.path.exists("batman.txt"):
#     print("File Exist")
# else:
#     print("File Not Found")

#--- Delete a file:

# os.remove("wonderwomen.txt")
