# 1. PANDAS BASICS
"""

# Pandas is a data manipulation and analysis tool that is built on Numpy.
# Pandas uses a data structure known as DataFrame (think of it as Microsoft excel in Python). 
# DataFrames empower programmers to store and manipulate data in a tabular fashion (rows and columns).
# Series Vs. DataFrame? Series is considered a single column of a DataFrame.

import pandas as pd
import numpy as np

# Let's define two lists as shown below:
mylist = ['aapl','tsla','azmz']

label = ['stock1','stock2','stock3']
type(label)

# Let's create a one dimensional Pandas "series" 
# Note that series is formed of data and associated labels 
xseries = pd.Series(data = mylist, index = label)
xseries

# Let's view the series
type(xseries)

# Let's define a two-dimensional Pandas DataFrame
# Note that you can create a pandas dataframe from a python dictionary
clientdf = pd.DataFrame({'BANK CLIENT ID':[111,222,333,444],
                         'BANK CLIENT NAME':['Chanel','Steve','Mitch','Robbie'],
                         
                         'NET WORTH [$]': [3500,29000,10000,2000],
                         'YEARS WITH BANK':[3,4,9,5]})

# Let's obtain the data type 
clientdf

# you can only view the first couple of rows using .head()
clientdf.head()

# you can only view the last couple of rows using .tail()
clientdf.tail()

"""**MINI CHALLENGE #1:**
- **A porfolio contains a collection of securities such as stocks, bonds and ETFs. Define a dataframe named 'portfolio_df' that holds 3 different stock ticker symbols, number of shares, and price per share (feel free to choose any stocks)**
- **Calculate the total value of the porfolio including all stocks**
"""

stockdf = pd.DataFrame({'TICKER':['AAPLE','TSLA','AMZN'],
                        'NUMBER OF SHARES':[3,5,9],
                        'PPS':[777,500,1700]})

total = stockdf['NUMBER OF SHARES']*stockdf['PPS']

total

totalstocks = total.sum()

totalstocks

print('total value of all stocks is ${}'.format(totalstocks))

"""# 2. PANDAS WITH CSV AND HTML DATA"""

# In order to access data on Google Drive, you need to mount the drive to access it's content

from google.colab import drive
drive.mount('/content/drive')

# Pandas is used to read a csv file and store data in a DataFrame
bankdf = pd.read_csv('/content/drive/MyDrive/1.1 Python for Financial Analysis - Course Package/Part 1. Python Programming Fundamentals/bank_client_information.csv')

bankdf

# write to a csv file without an index
bankdf.to_csv('example_out.csv', index = False)

# write to a csv file with an index
bankdf.to_csv('example_out2.csv', index = True)

# Read tabular data using read_html

housepricesdf = pd.read_html('https://www.livingin-canada.com/house-prices-canada.html')

housepricesdf[0]

housepricesdf[1]

"""**MINI CHALLENGE #2:**
- **Write a code that uses Pandas to read tabular US retirement data**
- **You can use data from here: https://www.ssa.gov/oact/progdata/nra.html** 
"""

retirement = pd.read_html('https://www.ssa.gov/oact/progdata/nra.html')

retirement[0]

"""# 3. PANDAS OPERATIONS"""

# Let's define a dataframe as follows:
clientdf = pd.DataFrame({'BANK CLIENT ID':[111,222,333,444],
                         'BANK CLIENT NAME':['Chanel','Steve','Mitch','Robbie'],
                         
                         'NET WORTH [$]': [3500,29000,10000,2000],
                         'YEARS WITH BANK':[3,4,9,5]})
clientdf

# Pick certain rows that satisfy a certain criteria 
dfloyal = clientdf[(clientdf['YEARS WITH BANK']>=5)]
dfloyal

"""**MINI CHALLENGE #3:**
- **Using "bank_client_df" DataFrame, leverage pandas operations to only select high networth individuals with minimum $5000** 
- **What is the combined networth for all customers with 5000+ networth?**
"""

networth = clientdf[(clientdf['NET WORTH [$]']>=5000)]
networth
networth['NET WORTH [$]'].sum()

"""# 4. PANDAS WITH FUNCTIONS"""

# Let's define a dataframe as follows:
clientdf = pd.DataFrame({'BANK CLIENT ID':[111,222,333,444],
                         'BANK CLIENT NAME':['Chanel','Steve','Mitch','Robbie'],
                         
                         'NET WORTH [$]': [3500,29000,10000,2000],
                         'YEARS WITH BANK':[3,4,9,5]})

# Define a function that increases all clients networth (stocks) by a fixed value of 10% (for simplicity sake) 
#* 1.1 # assume that stock prices increased by 10%

def nwupdate(balance):
  return balance *1.1

# You can apply a function to the DataFrame 

clientdf['NET WORTH [$]'].apply(nwupdate)

clientdf['BANK CLIENT NAME'].apply(len)

clientdf['YEARS WITH BANK'].sum()

"""**MINI CHALLENGE #4:**
- **Define a function that doubles stock prices and adds $100**
- **Apply the function to the DataFrame**
- **Calculate the updated total networth of all clients combined**
"""

def compound(x):
  return x*2+100

clientdf['NET WORTH [$]'].apply(compound)

clientdf['NET WORTH [$]'].sum()

"""# 5. SORTING AND ORDERING"""

# Let's define a dataframe as follows:
clientdf = pd.DataFrame({'BANK CLIENT ID':[111,222,333,444],
                         'BANK CLIENT NAME':['Chanel','Steve','Mitch','Robbie'],
                         
                         'NET WORTH [$]': [3500,29000,10000,2000],
                         'YEARS WITH BANK':[3,4,9,5]})

# You can sort the values in the dataframe according to number of years with bank
clientdf.sort_values(by = 'YEARS WITH BANK' )

# Note that nothing changed in memory! you have to make sure that inplace is set to True
clientdf.sort_values(by = ['YEARS WITH BANK'], inplace=True )

"""**MINI CHALLENGE #5:**
- **Sort customers by networth instead of years with bank. Make sure to update values in-memory.**
"""

clientdf.sort_values(by ='NET WORTH [$]')

clientdf.sort_values(by =['NET WORTH [$]'], inplace = True)

"""# 6. CONCATENATING AND MERGING WITH PANDAS

Check this out: https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
"""

df1 = pd.DataFrame({"A": ["A0", "A1", "A2", "A3"],
                    "B": ["B0", "B1", "B2", "B3"],
                    "C": ["C0", "C1", "C2", "C3"],
                    "D": ["D0", "D1", "D2", "D3"]},
index=[0, 1, 2, 3])

df2 = pd.DataFrame({"A": ["A4", "A5", "A6", "A7"],
                    "B": ["B4", "B5", "B6", "B7"],
                    "C": ["C4", "C5", "C6", "C7"],
                    "D": ["D4", "D5", "D6", "D7"]},
index=[4, 5, 6, 7])

df3 = pd.DataFrame({"A": ["A8", "A9", "A10", "A11"],
                    "B": ["B8", "B9", "B10", "B11"],
                    "C": ["C8", "C9", "C10", "C11"],
                    "D": ["D8", "D9", "D10", "D11"]},
index=[8, 9, 10, 11])

pd.concat([df1,df2,df3])

# Creating a dataframe from a dictionary
# Let's define a dataframe with a list of bank clients with IDs = 1, 2, 3, 4, 5 
rawdata = {'BANK CLIENT ID':[1,2,3,4,5],
           'FIRST NAME':['Nancy','Alex','Robbie','Matt','Diana'],
           'LAST NAME':['William','George','John','Dillon','Rapesatro']}

bankraw = pd.DataFrame(rawdata, columns = ['BANK CLIENT ID','FIRST NAME','LAST NAME'])
bankraw

# Let's define another dataframe for a separate list of clients (IDs = 6, 7, 8, 9, 10)
rawdata2 = {'BANK CLIENT ID':[6,7,8,9,10],
           'FIRST NAME':['Bill','Heather','Christina','Mo','Steve'],
           'LAST NAME':['Bob','Pickle','Hagu','Pasa','putki']}
bankraw2 = pd.DataFrame(rawdata2, columns = ['BANK CLIENT ID','FIRST NAME','LAST NAME'])
bankraw2

# Let's assume we obtained additional information (Annual Salary) about our bank customers 
# Note that data obtained is for all clients with IDs 1 to 10
rawnet = {'BANK CLIENT ID': [1,2,3,4,5,6,7,8,9,10],
          'Annual Salary [$/year]':[25000,45000,48000,65000,32000,33000,23000,78000,65000,120000]}
banksalary = pd.DataFrame(rawnet, columns = ['BANK CLIENT ID','Annual Salary [$/year]'])
banksalary

bankdfall = pd.concat([bankraw, bankraw2])

# Let's merge all data on 'Bank Client ID'
total = pd.merge(bankdfall,banksalary, on = 'BANK CLIENT ID')
total





"""**MINI CHALLENGE #6:**
- **Let's assume that you became a new client to the bank**
- **Define a new DataFrame that contains your information such as client ID (choose 11), first name, last name, and annual salary.**
- **Add this new dataframe to the original dataframe "bank_df_all".** 
"""

newclient = {'BANK CLIENT ID':[11],
           'FIRST NAME':['Mohgli'],
           'LAST NAME':['Wicked'],
           'Annual Salary [$/year':[100000]}
newbank = pd.DataFrame(newclient, columns = ['BANK CLIENT ID','FIRST NAME','LAST NAME','Annual Salary [$/year'])
newbank

newdf = pd.concat([total,newbank],axis=0)
newdf

"""# EXCELLENT JOB!

