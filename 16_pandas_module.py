# Pandas:
        # Pandas is the most popular python library for
        # Data analysis and manipulation.

        # It provides two main data structures:
            # 1) Series: 1- diamensional labeled array
            # 2) DataFrame: 2- diamensional table ( similar to SQL table or Excel Sheet)

    # Pandas is built on top of Numpy and is heavily used in:
            # Data Analysis
            # Data Cleaning
            # ETL Pipelines
            # Machine Learning
            # Financial Analysis
            # Reporting

#-----------------------------------------

# What to do to get panadas in system:
     # pip install pandas

import pandas as pd

# Create Series using Pandas:

# s1 = pd.Series([10, 20, 30])
# print(s1)

# s2 = pd.Series(("A", "B", "C"))
# print(s2)

# Cant use Set (because it is unordered)
# s3 = pd.Series(["A", 2, 3.4])
# print(s3)

# s4 = pd.Series([90, 50, 20], index=["A", "B", "C"])
# print(s4)
# print(s4["B"])

#------------------------------
# DataFrame:-
# df1 = pd.DataFrame({
#     "Name": ["Bhargav", "Swapna", "Hyndavi", "Rushil"],
#     "Age": [12, 9, 5, 40],
#     "Salary": [50000, 75000, 60000, 12000]
# }, index=["A", "B", "C", "D"])
# # NOTE: ValueError: All arrays must be of the same length
# print(df1)

#----------------------------
# What type of dtaatype is df1
# print(type(df1))  #<class 'pandas.DataFrame'>

# Attributes of Dataframe:
# print(df1.shape)
# print(df1.columns)
# print(df1.index)
# print(df1.dtypes)

#--------------------------------

import random
import pandas as pd

first_names = ["James","Mary","John","Patricia","Robert","Jennifer","Michael","Linda","William","Barbara",
               "David","Elizabeth","Richard","Susan","Joseph","Jessica","Thomas","Sarah","Charles","Karen",
               "Christopher","Lisa","Daniel","Nancy","Matthew","Betty","Anthony","Margaret","Mark","Sandra",
               "Donald","Ashley","Steven","Dorothy","Paul","Kimberly","Andrew","Emily","Kenneth","Donna",
               "Joshua","Michelle","Kevin","Carol","Brian","Amanda","George","Melissa","Timothy","Deborah"]

last_names = ["Smith","Johnson","Williams","Brown","Jones","Garcia","Miller","Davis","Wilson","Martinez",
              "Anderson","Taylor","Thomas","Hernandez","Moore","Martin","Jackson","Thompson","White","Lopez",
              "Lee","Gonzalez","Harris","Clark","Lewis","Robinson","Walker","Perez","Hall","Young",
              "Allen","Sanchez","Wright","King","Scott","Green","Baker","Adams","Nelson","Carter",
              "Mitchell","Perez","Roberts","Turner","Phillips","Campbell","Parker","Evans","Edwards","Collins"]

positions = ["Software Engineer","Senior Software Engineer","Data Analyst","Data Scientist","Product Manager",
             "HR Manager","Marketing Specialist","Sales Executive","DevOps Engineer","QA Engineer",
             "Business Analyst","UX Designer","Financial Analyst","Operations Manager","Team Lead"]

departments = ["Engineering","Data Science","Product","HR","Marketing","Sales","DevOps","QA","Finance","Operations","Design"]

salary_range = {
    "Software Engineer": (60000, 90000),
    "Senior Software Engineer": (90000, 130000),
    "Data Analyst": (55000, 80000),
    "Data Scientist": (85000, 120000),
    "Product Manager": (90000, 140000),
    "HR Manager": (60000, 95000),
    "Marketing Specialist": (50000, 75000),
    "Sales Executive": (55000, 100000),
    "DevOps Engineer": (80000, 120000),
    "QA Engineer": (55000, 85000),
    "Business Analyst": (60000, 90000),
    "UX Designer": (65000, 95000),
    "Financial Analyst": (65000, 95000),
    "Operations Manager": (70000, 110000),
    "Team Lead": (85000, 125000),
}

random.seed(42)
data = []

for i in range(100):
    pos = random.choice(positions)
    exp = random.randint(1, 20)
    age = random.randint(22, 55)
    sal_min, sal_max = salary_range[pos]
    salary = round(random.randint(sal_min, sal_max) + exp * 500, -2)

    data.append({
        "firstname": random.choice(first_names),
        "lastname": random.choice(last_names),
        "age": age,
        "position": pos,
        "department": random.choice(departments),
        "experience_years": exp,
        "salary": salary
    })

df = pd.DataFrame(data)
print(df.head(100))
