# String:-

    # Any charecter or sequence of charecters enclosed 
    # inside quotes are nothing but strings.

# name = 'hyndavi'
# print(name)
# print(type(name))  # str

        # Quotes can be of beloow types:
            # single quotes ==> ''
            # double quotes ==> ""
            # tripple single quotes ==> ''' '''
            # tripple double quotes ==> """ """

# password = 'kiran@123'
# print(password)
# print(type(password))  # str

# fruit = "Apple"
# print(fruit)
# print(type(fruit))  # str

# thought_of_the_day = '''Apple a day, keeps doctor away..'''
# print(thought_of_the_day)
# print(type(thought_of_the_day))


# thought_of_the_day_after_tomorrow = """Johny, Johny .. Yes Papa..!"""
# print(thought_of_the_day_after_tomorrow)
# print(type(thought_of_the_day_after_tomorrow))


# --------------------------

# xyz = 'Bhargav is the "tallest" among all'
# print(xyz)
# print(type(xyz))

# mno = "Hyndavi is the 'smartest' among all"
# print(mno)
# print(type(mno))


# para = '''Hello This is shiv from 'hyderababd'..!
# I am a "software engineer".
# You can also be a "software engineer".
# """learn python""" and get job..'''

# print(para)

# ------------What type of data type is String:-

    # String is sequesnce of charecters.
    # String is ordered datatypes 
    # String also supports indexing
    # String is Immutable Datatype  # Cant be update or modified

# x = 'Superman'

# INDEXING:

# name = "Sridhar"
# print(name)

# print(name[0])
# print(name[1])
# print(name[4])
# print(name[6])

# print(name[-7])
# print(name[-4])

#--------------------------------

# age = 56   # int
# weight = '77'  # str

# pqr = '1234567'
# print(pqr[6])
# print(pqr[10])  #IndexError: string index out of range


#--------------------------

# SLICING:-

friend = "Mallesh"
# print(friend)
# print(friend[3])

# les
# print(friend[3:6])  # [start: end]
# print(friend[-4:-1])

# Mleh
# friend = "Mallesh"
# print(friend[0:7:2]) # [start: end: step]  #Mleh
# print(friend[0::2])  #Mleh

# # as
# print(friend[1:6:4])


str1 = "ABCDEFGH"

# BEH
# print(str1[1:8:3])
# print(str1[0:6:5])
# print(str1[6::-3]) #GDA

str1 = "ABCDEFGH"
# # HGFE
# print(str1[-1:-5:-1])

# ABCD
# print(str1[0:4:1])
# print(str1[0:4:])

# ------------------- In-built Methods of string

# Functions ==> Methods

# Methods are useful to perform operations on object (string):

# Behind every method there is a program.

# Two types of Methods:
        # In Built Method
        # User Defined Methods

# str1 = "apple@123"

# Case Transformation Operations:

# .upper()  => Converts all lower case alphabets into uppercase.

# print(str1.upper())  #APPLE@123

# str2 = "GRAPE%8090"
# .lower()

# print(str2.lower())  #grape%8090

# str3 = "AjAy MisrA"
# print(str3.upper())  #AJAY MISRA
# print(str3.lower())  #ajay misra


# str4 = "davID warNer is the best BATSMAN"

# .title()  it converts strings each words first alphabetic letter to uppercae
# and rest of the letters to lowercase.

# print(str4.title()) #David Warner Is The Best Batsman


# .capitalize()  it converts only first letter of teh string to capital 
# and rest will be lowercase.

# str5 = "Donald TRUMP is the Best PresideNT Ever"
# print(str5.capitalize())  #Donald trump is the best president ever


# str6 = "PYTHON programming"
# .swapcase()  it converts uppercase letters into lowercase
# and lowercase into uppercase

# print(str6.swapcase())  #python PROGRAMMING


#--------------------------------------


# str7 = "   aaa8..AA"

# a.A
# print(str7[4:11:3])
# print(str7[-1:-8:-3].swapcase())

# ----------------- Search methods

# str8 = "kdjbdwbdieuwfwz 9eu3209j32j 39hd    2 hd3   28gy dhqehduygd"

# .index()  It seraches from left and returns the 
# first specified substring  index
# print(str8.index('d')) 

# # .rindex() this searches from right side
# print(str8.rindex('d'))  # 58

# print(str8.index('Z'))  #ValueError: substring not found


#-------------
# .find()  It seraches from left and returns the 
# first specified substring  index but 
# if substring is not available, it returns -1

# print(str8.find('d'))

# # .rfind()
# print(str8.rfind('d'))

# print(str8.find('Z'))  # -1
# print(str8.rfind('Z'))  # -1

#----------------------------

# .isdigit()
# .isalpha()
# .isalnum()

# str9 = "1234"
# print(str9.isdigit())

# str10 = "abcd"
# print(str10.isdigit())

# str11 = "klm123"
# print(str11.isdigit())

# str12 = "abcke"
# print(str12.isalpha())

# pstr13 = "gddTY."
# print(pstr13.isalpha())

# str14 = "123asd"
# print(str14.isalnum())

# str15 = "12345"
# print(str15.isalnum())

#---------------------------

# some other operations

# Repetation
s1 = "apple"
print(s1 * 2)


# concatination
s2 = "grape"
print(s1 + s2)


# packing & unpacking not supported by string
