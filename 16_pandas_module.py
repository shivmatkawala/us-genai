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
# print(df)

#--------------------
#groupby()
# print(df.groupby(
#     "department"
# )["salary"].sum())

# print(
#     df.groupby(
#         "position"
#     )["salary"].sum()
# )

# print(
#     df.groupby(
#         "department"
#     )["salary"].mean()
# )

# Get me avg experience by each department
# print(
#     df.groupby(
#         "department"
#     )["experience_years"].mean()
# )

#---------------------------------
# print(
#     df.groupby(
#         "department"
#     )["age"].mean()
# )

#----------------------------------------

# Exploratory Data Anaysis:
# describe()
# print(df.describe())

# print(df.head(20))
# print(df.tail(2))
# print(df)

# Accessing specific column

# print(df["position"])
# print(df["salary"])
# print(df[["firstname", "lastname", "age"]])

# Selecting Specific Rows:

# loc
# print(df.loc(1))
# print(df.iloc[0:2, 0:3])

# how to print powition, department, experiece_year 
# of 50 to 60 rows.
# print(df.iloc[50:61, 3:6])


# Filtering data:

# get all employees whose salary is above 100000
# print(df[df["salary"] > 100000])

# Get me all team leads
# print(df[df["position"] == "Team Lead"])

# Get me all DevOps Employees whose salary is less than 100000 whose age is bellow 30
# print(df[(df["department"] == "DevOps") & (df["salary"] < 100000) & (df["age"] < 30 )])

#--------------------------------------------
# Get me All employees whose age is bellow 30 
# or salary is less than 70000.

# print(
#     df[
#         (df["age"] < 30) |
#         (df["salary"] < 70000)
#     ]
# )

#--------------------------------------------
# Create New column called "Bonus" using 10% of salary

# df["bonus"] = df["salary"] * (10 / 100)

# df["take_home"] = df["salary"] + df["bonus"]

# print(df)

# Get me all those employees whose department is not "Marketing"
# and getting more than 150000 take_home

# print(
#     df[
#         (df["department"] != "Marketing") &
#         (df["take_home"] > 150000) 
#     ]
# )
#--------------------------------------------

# create dataframe:

# df1 = pd.DataFrame({
#     "pid": [101, 102, 103, 104],
#     "product": ["Oil", "Sugar", "Tea", "Coffe"],
#     "category": ["eadable", "sweet", "eadable", "sweet"]
# }, index=(0, 2, 4, 6))

# print(df1)
# print(df1.shape)
# print(df1.size)
# print(df1.index)
# print(df1.dtypes)


#-------------------------------------

# Updaing  Values:

# df1 = pd.DataFrame(
#     {
#         "Name": ["Rushil Patel", "Bhargav Patel", "Om Patil", "Swapna Repala", "Hyndavi Dharoor"],
#         "Age": [30, 45, 50, 20, 25],
#         "Marks": [90, 95, 100, 30, 25]
#     }
# )

# print(df1.drop(4))

# df1.loc[0, "Marks"] = None
# print(df1)

# df1.loc[2, "Age"] = 22
# df1.loc[3, "Marks"] = 150
# df1.loc[-2, "Marks"] = 15
# print(df1.drop("Marks", axis=1))   # Temperory delete
# df1.drop("Marks", axis=1, inplace=True) # Permanent delete
# print(df1)