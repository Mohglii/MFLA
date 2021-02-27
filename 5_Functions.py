"""5. Functions

# 1. BUILT-IN FUNCTIONS
"""
"""There are many built-in functions that you can leverage directly 
Let's define 2 lists x and y"""

x = [4,5,1,2,8,6]
y = list(range(1,7))

"""basic built-in functions"""
print(len(y))  #how many int are in list 
print(min(x))  #min - print lowest value 
print(max(x))  #max - 

# Let's create a tuple out of the list

#      *tuples are immutable, meaning the cannot overwrite values
z=tuple(x)
print(z)
print(type(z))

 # Let's obtain the sum of elements in x
print(sum(x))  # sum - add all values in list


"""**MINI CHALLENGE #1:**
- **Write a code that takes in 2 lists x = [-1 -4 -7] and y = [-3 7 4] and  calculates the absolute sum of all its elements |x+y|**"""
x = [-1, -4, -7]
y = [-3, 7, 4]

# a = x + y
# z = [abs(ele) for ele in a]
# print(sum(z))

z= (abs(sum(x+y)))
print(z)






"""# 2. FUNCTIONS"""

# Let's define a function named "my_function" that does not receive any arguments
# The function simply prints out content and does not return anything


# Function call
def myfunction():
    print('i will pass ftmo and fundingtalent verification challenges ')
    
myfunction()                                      #printing functions donot need print()... simply enter function name ....'funcation call'

# Define a function that takes in argument x and return the squared value
def squared(x):
    return (x**2)
out = (squared(3))   #send value into x...this is var assignment 
# # Call the function
def squared2(x, out=3):
    return(x**2+out)
print(squared2(12))

# # Define a function with default value
def func(amount= 0.0):
    print('my total portfolio worth is equal to: ${}'.format(amount))
func(1000)

# # If you pass an argument to the function, it overwrites the default value
func(4000)

# # If you don't pass an argument, the default value "20000" will be used instead
func()
func(20000)
"""**MINI CHALLENGE #2:** 
- **Write a code that takes in two inputs (number of shares and prices) from the user and calculate the total account balance**
"""

shares = input('How many shares do you own?')
price = input('Enter the price per share')
def total(shares, price = 200):
    totalvalue = int(shares) * int(price)
    print(f'The total value of your portfolio is ${totalvalue}.')
total(shares, price)


"""# 3. LAMBDA EXPRESSIONS """

# Lambda function is used to create a function without a name 
# Lambda functions are mainly used with filter() and map() [they will be discussed later on]. 
# Lambda function can receive any number of arguments, but can only have one expression.


# # let's see how to create a basic function that squares the input
number = int(input('enter a number'))
def base(number):
    squared = number**2
    print(f'The squared value of {number} is {squared}.')
# # Function call
base(number)

# We can do the same task using Lambda expression

x = int(input('Enter a number:'))
y= lambda x:x**2
print(f'the value of {x} is {y(x)}')
# Note that there is no function name

# Note that lambda expression can take in more than one argument 
# there is only one expression that could be performed

def sumation(x,y,z):
    return x+y+z
result = sumation(1,2,3)
print(result)

p = lambda x,y,z : x+y+z
print(p(1,2,3))

"""**MINI CHALLENGE #3:**
- **Repeat mini challenge #2 (Write a code that takes in two inputs from the user and calculates the total) using lambda expressions instead**
"""

shares = int(input('How many shares do you own?'))
price = int(input('Enter the price per share'))
total = lambda shares,price : (shares) * (price)

#.format method
print('total = ${}.'.format(total(shares,price)))
#fstring method 
print(f'the total is: ${total(shares, price)}')




"""# 4. MAP """

# The map() function takes in a function and a list.
# map() performs an operation on the entire list and return the results in a new list.
# Define two lists a and b

a = [ 1,4,5,6,9]
b = [1,7,9,12,7]

# # Let's define a function that adds two elements together

def sum(a,b):
    return a+b

# You can now use map() to apply a function to the entire list and generate a new list
c = list(map(sum, a,b))
print(c)

# map could be used with Lambda as follows
# lambda function is an anonymous function that take any number of arguments and can only have one expression
number = [1,2,3,4,5,6,7,8,9,]

num2 = list(map(lambda x :x**2, number))
print(num2)



"""**MINI CHALLENGE #4:**
- **Write a function that takes an argument and return its cubic value**
- **Define a list of integers ranging from -10 to 10** 
- **Apply the function to the entire list and generate a new output list** 


def cubic(x):
    return x*x*x

num = list(range(-10,11))

num2 = list(map(lambda x :cubic(x),num))
print(num2)



# """# 5. FILTER
# """
# # filter is used to create a list of elements for which a function returns "True".
prices= [105, 5005, 173, 356, 922, 1443,22, 202]

even = list(filter(lambda x: (x%2==0), prices))

print(even)


odd = list(filter(lambda x : (x%3 ==0), prices))
print(odd)


# # Return prices that are greater than or equal 100

over_100 = list(filter(lambda x: (x>=100),prices))
print(over_100)



# # Return age between 200 and 250


k = list(filter(lambda x: (x>=200 and x<=300),prices))
print(k)

"""**MINI CHALLENGE #5:**
- **Write a code from the user that takes in a range (upper and lower bounds) and returns a list of positive and even numbers only** 

"""

number1 = int(input('enter a number below 0 no less than -50:'))
number2 = int(input('enter a number below 0 no less than 50:'))
number3= list(range(number1,number2))
pos = list(filter(lambda x : (x>=0 and x%2==0), number3))
print(pos)


