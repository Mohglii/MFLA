# """10. Seaborn 


# # 1. SEABRON SCATTERPLOT & COUNTPLOT
# """

# # Seaborn is a visualization library that sits on top of matplotlib
# # Seaborn offers enhanced features compared to matplotlib
# # https://seaborn.pydata.org/examples/index.html
# # import libraries
import numpy as np
import os 
import matplotlib.pyplot as plt
import pandas as pd 
# Seaborn is a visualization library that sits on top of matplotlib...
import seaborn as sns

# np.C_ class object translates slice objects to concatenation along the second axis.
x1 = np.array([1,2,3])
x1.shape
x2 = np.array([4,5,6])
x2.shape

z = np.c_[x1,x2]
z

# #                    np.c_ will pair lists by the index value  in a vertical fashion as such: 
# #array([[1, 4],
#        #[2, 5],
#        #[3, 6]])

# # Seaborn is a visualization library that sits on top of matplotlib...
# Import Cancer data drom the Sklearn library


# #scikit library have preconditioned data sets 
# #used for machine learning with many algorithms 

from sklearn.datasets import load_breast_cancer

# #%%
import numpy as np
import os 
import matplotlib.pyplot as plt
import pandas as pd 
# Seaborn is a visualization library that sits on top of matplotlib...
import seaborn as sns
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
print(cancer)



# # Create a dataFrame named df_cancer with input/output data
cancerdf = pd.DataFrame(np.c_[cancer['data'],cancer['target']], columns = np.append(cancer['feature_names'],['target']))
cancerdf


# # Check out the head of the dataframe
cancerdf.head()
# # Check out the tail of the dataframe
cancerdf.tail()


# # Plot scatter plot between mean area and mean smoothness
# # sns.scatterplot(x='mean area', y='mean smoothness',hue = 'target', data = cancerdf)
# # Let's print out countplot to know how many samples belong to class #0 and #1
# # sns.countplot(cancer['target'])
# # """**MINI CHALLENGE #1:**
# # - **Plot the scatterplot between the mean radius and mean area. Comment on the plot** 

# # """
# cancerdf
sns.scatterplot(x='mean radius',y='mean area', hue = 'target', data = cancerdf)


# """# 2. SEABORN PAIRPLOT, DISPLOT, AND HEATMAPS/CORRELATIONS"""
#%%
import numpy as np
import os 
import matplotlib.pyplot as plt
import pandas as pd 
# Seaborn is a visualization library that sits on top of matplotlib...
import seaborn as sns
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
print(cancer)
cancerdf = pd.DataFrame(np.c_[cancer['data'],cancer['target']], columns = np.append(cancer['feature_names'],['target']))

# Plot the pairplot
sns.pairplot(cancerdf, hue = 'target', vars = ['mean radius','mean texture','mean area','mean perimeter','mean smoothness'])

# Strong correlation between the mean radius and mean perimeter, mean area and mean primeter
plt.figure(figsize = (20,10))
sns.heatmap(cancerdf.corr(),annot =  True)

# plot the distplot 

# Displot combines matplotlib histogram function with kdeplot() (Kernel density estimate)
# KDE is used to plot the Probability Density of a continuous variable.

sns.distplot(cancerdf['mean radius'], bins = 24, color = 'b')
# """**MINI CHALLENGE #2:**
# - **Plot two separate distplot for each target class #0 and target class #1**
# """
class0 = cancerdf[cancerdf['target'] == 0]
class1 = cancerdf[cancerdf['target'] == 1]
plt.figure(figsize=(10,7))
sns.distplot(class0['mean radius'], bins =25, color= 'blue')
sns.distplot(class1['mean radius'], bins = 25, color = 'red')
plt.grid()






# """# EXCELLENT JOB!

# # MINI CHALLENGE SOLUTIONS:

# **MINI CHALLENGE #1 SOLUTION:**
# - **Plot the scatterplot between the mean radius and mean area. Comment on the plot**
# """

# sns.scatterplot(x = 'mean radius', y = 'mean area', hue = 'target', data = df_cancer)
# # As mean radius increases, mean area increases 
# # class #0 generally has larger mean radius and mean area compared to class #1

# """**MINI CHALLENGE #2 SOLUTION:**
# - **Plot two separate distplot for each target class #0 and target class #1**

# """

# class_0_df = df_cancer[ df_cancer['target']==0 ]
# class_1_df = df_cancer[ df_cancer['target']==1 ]

# class_0_df

# class_1_df

# # Plot the distplot for both classes
# plt.figure(figsize=(10, 7))
# sns.distplot(class_0_df['mean radius'], bins = 25, color = 'blue')
# sns.distplot(class_1_df['mean radius'], bins = 25, color = 'red')
# plt.grid()
# %%
 