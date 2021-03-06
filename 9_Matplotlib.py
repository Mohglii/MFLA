# """9. Python 101 - Data Visualization with matplotlib 
#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import csv
import os
from pandas.io.parsers import read_csv
# # 1. BASIC LINE PLOT
# """
stockdf = pd.read_csv('/Users/mohgli/Desktop/Python/a) The Complete Python & Machine Learning for Financial Analysis/1.1 Files/stocks.csv')
stockdf
stockdf.plot( x = 'Date', y = 'AAPL', label = 'Apple Stock Prices', linewidth=3)
plt.ylabel('Price')
plt.legend(loc = 'upper right')
plt.title('First Plot:)')

"""**MINI CHALLLENGE #1:**
- **Plot similar kind of graph for the S&P500**
- **Change the line color to red**
"""

stockdf.plot(x='Date',y='sp500', label= 'SP500 Stock Prices', linewidth=3, color = 'red')
plt.ylabel('Price')
plt.legend('upper left')

"""# 2. SCATTERPLOT """

# Read daily return data using pandas
returnsdf = pd.read_csv('/Users/mohgli/Desktop/Python/a) The Complete Python & Machine Learning for Financial Analysis/1.1 Files/daily_returns.csv')
returnsdf

x = returnsdf['AAPL']
y = returnsdf['sp500']


plt.scatter(x, y)
plt.xlabel('Apple Returns')
plt.ylabel('sp500 returns')


# # """**MINI CHALLLENGE #2:**
# # - **Plot similar kind of graph for GOOG and sp500**
x = returnsdf['GOOG']
y = returnsdf['sp500']
plt.scatter(x, y)
plt.scatter(x, y)
plt.xlabel('Google Returns')
plt.ylabel('sp500 returns')
# # """
using these kind of charts we can perform calucaltions to recieve relationship metrics and perform regression

"""# 3. PIE CHART"""


values = [20,55,5,17,3]
colors = ['g','r','y','b','m']
lab = ['AAPL','Google','T','Tesla','Amazon']
explode = [0, 0.2,0,0,0]
plt.figure(figsize = (7,7))
plt.pie(values, colors=colors, labels=lab, explode= explode)
plt.title('Stock Portfolio')
explode method will allow user to emphasize certain data on pie charts... explode must be defined as a list index 

"""**MINI CHALLENGE #3:**
- **Plot the pie chart for the same stocks assuming equal allocation**
- **Explode Amazon and Google slices**

"""
values = [20,20,20,20,20]
colors = ['g','r','y','b','m']
lab = ['AAPL','Google','T','Tesla','Amazon']
explode = [0, 0.1,0,0,0.1]
plt.figure(figsize = (7,7))
plt.pie(values, colors=colors, labels=lab, explode= explode)
plt.title('Stock Portfolio')"""


""" 4. HISTOGRAMS"""

"""A histogram represents data using bars of various heights. 
Each bar groups numbers into specific ranges. 
Taller bars show that more data falls within that specific range."""
returnsdf

"""print histogram of apple returns in a histogram format 
calculate mean of distribution
calculate standard deviation of distribution ( standard devaiation - dispersion away from mean )"""


mu = returnsdf['AAPL'].mean()
sigma = returnsdf['AAPL'].std()
numbins=40
plt.figure(figsize= (7,5))
plt.hist(returnsdf['AAPL'], numbins)
plt.grid()
plt.title('Histogram: mu= ' + str(mu) + ', sigma=' + str(sigma))
"""**MINI CHALLLENGE #4:**
- **Plot the histogram for GOOG returns using 30 bins**
# """
#%%
returnsdf = pd.read_csv('/Users/mohgli/Desktop/Python/a) The Complete Python & Machine Learning for Financial Analysis/1.1 Files/daily_returns.csv')
returnsdf

mu = returnsdf['GOOG'].mean()
sigma = returnsdf['GOOG'].std()
numbins = 40
plt.figure(figsize=(7,5))
plt.hist(returnsdf['GOOG'],numbins)
plt.grid()
plt.xlabel('Mean std of distribution')
plt.title('Histogram: mu= '+str(mu)+', sigma='+ str(sigma))


"""# 5. MULTIPLE PLOTS"""
%%
stockdf = pd.read_csv('/Users/mohgli/Desktop/Python/a) The Complete Python & Machine Learning for Financial Analysis/1.1 Files/stocks.csv')
stockdf


stockdf.plot(x ='Date', y=['AAPL','sp500'], linewidth = 3)
plt.ylabel('Price')
plt.title('Stock Prices')
plt.grid()

"""**MINI CHALLLENGE #5:**
- **Plot a similar graph containing prices of AAPL, sp500 and GOOG**
- **Add legend indicating S&P500, AAPL and GOOG**
- **Place the legend in the "upper center" location** 

"""
stockdf.plot(x= 'Date', y= ['AAPL','sp500','GOOG'])
plt.ylabel('Prices of Stock from 01/12 to 12/12')
# plt.legend()
plt.legend(loc = 'upper center')

"""# 6. SUBPLOTS"""
#%%
stockdf = pd.read_csv('/Users/mohgli/Desktop/Python/a) The Complete Python & Machine Learning for Financial Analysis/1.1 Files/stocks.csv')

plt.figure(figsize = (8,5))
# specificy naming convention by printing 2 subplots 
plt.subplot(1,2,1)
plt.plot(stockdf['AAPL'], linewidth = 2, color = 'r')
plt.grid()
plt.subplot(1,2,2)
plt.plot(stockdf['sp500'],linewidth = 2, color = "b")
plt.grid()

how to create a subplot in a vertical visual
#%%
plt.figure(figsize=(8,8))
plt.subplot(2,1,1)
plt.plot(stockdf['AAPL'], linewidth = 2, color = 'r')
plt.grid()
plt.subplot(2,1,2)
plt.plot(stockdf['sp500'],linewidth = 2, color = "b")
plt.grid()
# """**MINI CHALLLENGE #6:**
# - **Create subplots like above for GOOG, AAPL and sp500**
# """
#%%
plt.figure(figsize = (6,6))
plt.subplot(3,1,1)
plt.plot(stockdf['AAPL'], linewidth = 2, color = 'r')
plt.legend('apple Price')
plt.subplot(3,1,2)
plt.plot(stockdf['GOOG'], linewidth = 2, color = 'b')
plt.legend('goog Price')
plt.subplot(3,1,3)
plt.plot(stockdf['sp500'], linewidth = 2, color = 'g')
plt.legend('sp500 Price')






"""# 7. 3D PLOTS"""
"""Toolkits are collections of application-specific functions that extend Matplotlib.
mpl_toolkits.mplot3d provides tools for basic 3D plotting.
https://matplotlib.org/mpl_toolkits/index.html"""

"""**MINI CHALLLENGE #7:**
- **Create a 3D plot with daily return values of sp500, GOOG and AAPL**
# """
#%%

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection = '3d')
x=[1,2,3,4,5,6,7,8,9,10]
y=[5,6,2,3,13,4,1,2,4,8]
z=[2,3,3,3,5,7,9,11,9,10]
ax.scatter(x,y,z, c = "r", marker = 'o')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

"""**MINI CHALLLENGE #7:**
- **Create a 3D plot with daily return values of sp500, GOOG and AAPL**  
#%%


stockdf = pd.read_csv('/Users/mohgli/Desktop/Python/a) The Complete Python & Machine Learning for Financial Analysis/1.1 Files/stocks.csv')
fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot(111, projection = '3d')
x= stockdf['AAPL'].tolist()
y= stockdf['GOOG'].tolist()
z= stockdf['sp500'].tolist()
ax.scatter(x,y,z, c = "b", marker = 'o')
ax.set_xlabel('x label')
ax.set_ylabel('y label ')
ax.set_zlabel('z label')




"""# 8. BOXPLOTS"""

# numpy.random.normal() takes three arguments: mean, standard deviation of the normal distribution, and number of values desired.
# Great resource: https://stackoverflow.com/questions/17725927/boxplots-in-matplotlib-markers-and-outliers

#%%
np.random.seed(20)
import numpy as np

np.random.seed(20)
data1=np.random.normal(200,20,20000)
data2=np.random.normal(60,30,20000)
data3=np.random.normal(70,20,20000)
data4=np.random.normal(40,5,20000)

data = [data1,data2,data3,data4]
fig = plt.figure(figsize= (10,7))
ax=fig.add_subplot(111)
bp = ax.boxplot(data)





"""**MINI CHALLENGE #8:**
- **Plot the box plot for  a new dataset data_5 that is normally distributed with an average of 800 and standard deviation = 100**
"""

#%%
np.random.seed(20)
data1=np.random.normal(200,20,20000)
data2=np.random.normal(60,30,20000)
data3=np.random.normal(70,20,20000)
data4=np.random.normal(40,5,20000)
data5=np.random.normal(800,100,2000)
data = [data1,data2,data3,data4,data5]
fig = plt.figure(figsize= (10,7))
ax=fig.add_subplot(111)
bp = ax.boxplot(data)


# %%
