"""7_Python Libraries for Data Analysis

# 1. NUMPY BASICS
"""

"""NumPy is a Linear Algebra Library used for multidimensional arrays
NumPy brings the best of two worlds: (1) C/Fortran computational efficiency, (2) Python language easy syntax """
import numpy as np 
mylist =[10,20,50,60,70]
print(mylist)

# Let's define a one-dimensional array
mylist =[10,20,50,60,70]
print(mylist)

# Let's create a numpy array from the list "my_list"
x = np.array(mylist)
print(x)

# Multi-dimensional (Matrix definition)

print(type(x))
matrix = np.array([[5,8],[9,13]])
print(matrix)

"""**MINI CHALLENGE #1:** 
- **Write a code that creates the following 2x4 numpy array**

```
[[4 6 8 7] 
[20 5 6 9]]
# # ```
# # """

# challenge = np.array([[4,6,8,7], [20,5,6,9]])
# print(challenge)


# """# 2. BUILT-IN METHODS AND FUNCTIONS """

 # "rand()" uniform distribution between 0 and 1
x = np.random.rand(15)
print(x)
# you can create a matri x of random number as well
xx = np.random.rand(5,5)
print(xx)
# # "randn()" normal distribution between 0 and 1
xxx= np.random.randn(10)
print(xxx)


#single random integer 
# # "randint" is used to generate random integers between upper and lower bounds
a= np.random.randint(1,10)
print(a)
# multiple random integers
aa = np.random.randint(1,100,15)
print(aa)



#even distribution

# # np.arange creates an evenly spaced values within a given interval
b = np.arange(1, 50)
print(b)
# Create an evenly spaced values with a step of 5
bb = np.arange(1, 50, 5)
print(bb)




# create a diagonal of ones and zeros everywhere else
covariance and matrix matrices and stock predictions
c = np.eye(15)
print(c)
# # Array of ones
cc= np.ones(10)
print(cc)
# # Matrices of ones
ccc= np.ones((15,15))
print(ccc)
# # Array of zeros
d = np.zeros(50)
print(d)

"""**MINI CHALLENGE #2:**
- **Write a code that takes in a number x from the user
    creates a 1x20 array with random numbers ranging from 0 to x**
# """

# x = int(input('enter a random number: '))
# xx = np.random.randint(1,x,20)
# print(xx)


"""# 3. SHAPE, LENGTH, TYPE, RESHAPE, AND MAX/MIN VALUES"""

"""Let's define a one-dimensional array"""
mylist = [-30,4,50,60,29,15,22,90]
x = np.array(mylist)


# """Get Length of a numpy array
print(len(x))
# Get shape
print(x.shape)
 
# Obtain the datatype
print(x.dtype)

# Reshape 1D array into a matrix
z = x.reshape(2,4)
print(z)


# Obtain the maximum element (value)
print(x.max())
# Obtain the minimum element (value)
print(x.min())
Obtain the location of the max element
print(x.argmax)

# Obtain the location of the min element"""
print(x.argmin)


# """**MINI CHALLENGE #3:**
# - **Write a code that creates a 4x5 array inwhich numbers range between 300 and 500 such that the difference between elements is 10**
# # """

x = list(range(300,500,10))
xx = np.array(x)
xxx = xx.reshape(4,5)
print(xxx)


# "# """**MINI CHALLENGE #4:**
"""- **Write a code that creates a 20x20 numpy array of random values that ranges from -1000 to 1000 and obtain the maximum, minimum, and mean values** 
"""
g = np.random.randint(-1000,1000,(20,20))
print(g.max())
print(g.min())
print(g.mean())

"""# 4. MATHEMATICAL OPERATIONS"""

x = np.arange(1,10)
y = np.arange(1,10)
zysum = x+y

#sqaure
squared = x**2
print(squared)

#square root
sqrt = np.sqrt(squared)
print(sqrt)

#exponential value for np array 
z = np.exp(y)
print(z)


"""**MINI CHALLENGE #5:**
- **Given the X and Y values below, obtain the distance between them**

x = [3,20,30]
y = [4,6,7]

xx=np.array(x)
yy=np.array(y)

distance = np.sqrt(xx+yy)
print(distance)




"""# 5. SLICING AND INDEXING """
x = np.array([20,40,50,21,15])


# # Access specific index from the numpy array
print(x[0])
# # Starting from the first index 0 up until and NOT inlcluding the last element
print(x[0:5])

# # Broadcasting, altering several values in a numpy array at once
x[0:2] = 10
print(x)

# Let's define a two dimensional numpy a"rray
matrix = np.random.randint(1,10,(5,5))
 
#access a row 
matrix[2]

#specific element
matrix[0][2]
matrix[0][3]

#obtain multiple rows in a mini matrix 
mm= matrix[:3]
print(mm)

#obtain a series of rows with specified columns 
mini = matrix[:,2:]
print(mini)

# """**MINI CHALLENGE #6:**
# - **In the following matrix, replace the last row with -1**
# - **Multiply the 2x2 matrix in the upper right corner by 2**"""

x = np.array([
    [2, 30, 20, -2, -4],
    [3, 4,  40, -3, -2],
    [-3, 4, -6, 90, 10], 
    [25, 45, 34, 22, 12],
    [13, 24, 22, 32, 37],
    ])

x[4] = -1
x[:2,3:] =x[:2,3:] *2
print(x)



# 6. ELEMENTS SELECTION (CONDITIONAL)

"""how to select specific elements witin  a np.array that satisfies conditional criteria"""
matrix = np.random.randint(1,10,(5,5))
#lets say i need to obtain elements that are greater than 3 only 
new = matrix[matrix>3]

#lets say i need to obtain elements that are less than 4 only 
new2 = matrix[matrix<4]

#lets say i need to obtain elements that are even only
new3 = matrix[matrix%2==0]

#lets say i need to obtain elements that are odd only
new4 = matrix[matrix%3==0]
"""**MINI CHALLENGE #7:**
- **In the following matrix, replace negative elements by 0 and replace odd elements with 25**"""

x = np.array([
    [2, 30, 20, -2, -4],
    [3, 4,  40, -3, -2],
    [-3, 4, -6, 90, 10], 
    [25, 45, 34, 22, 12],
    [13, 24, 22, 32, 37],
    ])


x[x%2==1]=25
x[0>x]=0
print(x)

