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

s1 = pd.Series([10, 20, 30])
print(s1)

s2 = pd.Series(("A", "B", "C"))
print(s2)

# Cant use Set (because it is unordered)
s3 = pd.Series(["A", 2, 3.4])
print(s3)

s4 = pd.Series([90, 50, 20], index=["A", "B", "C"])
print(s4)

