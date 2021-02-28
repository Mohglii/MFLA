"""7_Python Libraries for Data Analysis

# 1. NUMPY BASICS
"""

# NumPy is a Linear Algebra Library used for multidimensional arrays
# NumPy brings the best of two worlds: (1) C/Fortran computational efficiency, (2) Python language easy syntax 
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
```
"""

challenge = np.array([[4,6,8,7], [20,5,6,9]])
print(challenge)


# """# 2. BUILT-IN METHODS AND FUNCTIONS """

# # "rand()" uniform distribution between 0 and 1
x = np.random.rand(15)
print(x)
numbers generated from uniform distribution

# you can create a matrix of random number as well
xx = np.random.rand(5,5)
print(xx)

# # "randn()" normal distribution between 0 and 1

xxx= np.random.randn(10)
print(xxx)

# # "randint" is used to generate random integers between upper and lower bounds

x2 = np.random.randint(1,10)
print(x2)

x3= np.random.randint(1,100,15)
print(x3)

# # np.arange creates an evenly spaced values within a given interval
a = np.arange(1,50)
print(a)

# Create an evenly spaced values with a step of 5
aa = np.arange(1,50,5)
print(aa)
# # create a diagonal of ones and zeros everywhere else
b = np.eye(15)
print(b)
# # Array of ones
bb = np.ones(10)
print(bb)
# # Matrices of ones
bbb = np.ones((15,15))
# # Array of zeros
c = np.zeros(50)
print(c)


"""**MINI CHALLENGE #2:**
- **Write a code that takes in a number x from the user
    creates a 1x20 array with random numbers ranging from 0 to x**
# """

inp = int(input('enter a number?: '))
inpp = np.random.randint(1,inp,20)
print(inpp)



"""# 3. SHAPE, LENGTH, TYPE, RESHAPE, AND MAX/MIN VALUES"""

# Let's define a one-dimensional array

"""Get Length of a numpy array

Get shape

Obtain the datatype

Reshape 1D array into a matrix

Obtain the maximum element (value)

Obtain the minimum element (value)

Obtain the location of the max element

Obtain the location of the min element"""

"""**MINI CHALLENGE #3:**
- **Write a code that creates a 4x5 array inwhich numbers range between 300 and 500 such that the difference between elements is 10**
# """

b = list(range(300,500,10))
c = np.array(b)
d = c.reshape(4,5)
print(d)
# print(x3)

c = np.array
print(c)


# "# """**MINI CHALLENGE #4:**
"""- **Write a code that creates a 20x20 numpy array of random values that ranges from -1000 to 1000 and obtain the maximum, minimum, and mean values** 
"""

b = np.arange(-1000,1000,10)
print(b)
# print(x3)


x = np.random.randint(-1000,1000,(20,20))
print(x.max())
print(x.min())
print(x.mean())
v3 = v2.reshape(20,20)
print(v3)



"""# 4. MATHEMATICAL OPERATIONS"""
# np.arange() returns an evenly spaced values within a given interval

x= np.arange(1,10)
y= np.arange(1,10)
# sum = x+y

squared = x**2
print(squared)

sqrt= np.sqrt(squared)

print(sqrt)

z= np.exp(sqrt)
print(z)


"""**MINI CHALLENGE #5:**
- **Given the X and Y values below, obtain the distance between them**
x = [3, 20, 30]
y = [4, 6, 7]
x=np.array(x)
y=np.array(y)
z= np.sqrt(x**2+y**2)
print(z)

"""# 5. SLICING AND INDEXING """

x = np.array([20,40,50,21,15])
# # Access specific index from the numpy array
print(x[0])
print(x[2])
# # Starting from the first index 0 up until and NOT inlcluding the last element
print(x[0:3])
# # Broadcasting, altering several values in a numpy array at once
x[0:4]=54
# print(x)

# Let's define a two dimensional numpy a"rray
matrix = np.random.randint(1,10,(5,5))
# print(matrix)
# # print()


# print(matrix[4][2])

# print(matrix[2])

# list3 = []
# list3.append(matrix[4][2])
# print(list3)

create a 'mini matrix' (sublist from larger matrix)
#slice all elements from 0-3
matrix = np.random.randint(1,10,(5,5))
minimatrix = matrix[:3]
print(minimatrix)

mm2= matrix[:,2:]
print(mm2)


mm3=matrix[:,:2]
print(mm3)
"""**MINI CHALLENGE #6:**
- **In the following matrix, replace the last row with -1**
- **Multiply the 2x2 matrix in the upper right corner by 2**



x = np.array([
    [2, 30, 20, -2, -4],
    [3, 4,  40, -3, -2],
    [-3, 4, -6, 90, 10], 
    [25, 45, 34, 22, 12],
    [13, 24, 22, 32, 37],
    ])
x[4]=(-1)
x[:2,3:5]= x[:2,3:5]*2
print(x)


# 6. ELEMENTS SELECTION (CONDITIONAL)
"""
"""how to select specific elements witin  a np.array that satisfies conditional criteria"""
matrix = np.random.randint(1,10,(5,5))
#lets say i need to obtain elements that are greater than 3 only 
newm= matrix[matrix>3]
print(newm)
#lets say i need to obtain elements that are less than 4 only 
newm2  = matrix[matrix<=4]
print(newm2)
#lets say i need to obtain elements that are even only
newm3 = matrix[matrix%2==0]
print(newm3)
#lets say i need to obtain elements that are odd only
newm4 = matrix[matrix%3==0]
print(newm4)

"""**MINI CHALLENGE #7:**
- **In the following matrix, replace negative elements by 0 and replace odd elements with 25**"""


x = np.array([[2, 30, 20, -2, -4],
              [3, 4,  40, -3, -2],
              [-3, 4, -6, 90, 10],
              [25, 45, 34, 22, 12],
              [13, 24, 22, 32, 37]])

x[x%2==1]=25
x[x<0]=0
print(x)