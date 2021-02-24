
# some code was commented out 





# # """3. Python 101 - Comparison, Logical Operators, Conditional Statements - Skeleton.ipynb
# # # 1. COMPARISON OPERATORS
# # """

# # # Comparison Operator output could be "True" or "False"
# # # Let's cover equal '==' comparison operator first
# # # It's simply a question: "Is stock_1_price equals stock_2_price or not?"
# # # "True" output means condition is satisfied 
# # # "False" output means Condition is not satisfied (condition is not true)
# # stock1price= 1000
# # stock2price= 1000
# # print(stock1price == stock2price)

# # #== is a comparison operator and = is used to as an assignment 
# # # Note that '==' is a comparison operator 
# # # Note that '=' is used for variable assignment (put 10 in stock_1_price)
# # stock1price= 1000
# # stock2price= 2000
# # print(stock1price == stock2price)

# # # Greater than or equal operator '>='
# # stock1price= 5000
# # stock2price= 1000
# # print(stock1price >= stock2price)

# # # Comparison operators work with strings as well
# # print('finance' == 'finance')
# # print('apple' == 'Apple')
# # # Both strings have to exactly match (lower case vs. upper case)

# # # Not equal comparison operator '!='
# # stock1price= 1000
# # stock2price= 1000
# # print(stock1price != stock2price)

# """**MINI CHALLENGE #1:**
# - **Without executing the code cell, What will this code generate?**

# ```
# stock_1_price = 15
# stock_2_price = 10

# print(stock_1_price == stock_2_price) 
# print(stock_1_price != stock_2_price) 
# print(stock_1_price > stock_2_price)
# print(stock_1_price < stock_2_price) 
# ```

# """
# # false 
# # true
# # true
# # false 



# # """# 2. LOGICAL OPERATORS"""

# # # For "and" logical operators, both arguments must be "True" in order for the output to be "True" 
# # # (Note that this is the only case in which the 'and' logical operator generates a True output)
# # # 1 and 1 = 1

# """
# for logical operators arguements must be true for the output to be true

# 'and' - both conditions must be true 
# """
# # # 0 and 1 = 0
# # # 0 and 0 = 0

 

# """For "or" logical operators, if any one of the arguments is "True", the output will be "True" 
# 'or' - only one stmt must be true
# TRUE
# # # 1 or 1 = 1
# # # 1 or 0 = 1
# # # 0 or 1 = 1

# FALSE
# 0 or 0 = 0 (Note that this is the only case in which the 'or' logical operator generates a False output)
# True and False = False
# True or False = True"""

# a = (10 > 3) and (9==3)
# print(a)

# b = (9>3) or (12 == 10)
# print(b) 


# """**MINI CHALLENGE #2:**
# - **Without executing the code cell, What will these two lines of code generate?**
# ```
# print('FINANCE'!='FINANCE' and (10 > 3) and (20 == 20)) 
# ```
# ```
# print('Finance'!='FINANCE' or (16 > 20) or (25 == 25)) 
# ```
# **MINI CHALLENGE #3:**
# - **Without executing the code cell, What will these two lines of code generate?**
# ```
# a = 5
# b = 3.5
# print(a == b or a != b) 
# print(a == b and a != b) 
# ```
# """



# """# 3. CONDITIONAL STATEMENTS
# - A simple if-else statement is written in Python as follows:
# ```
# if condition:
#   statement #1
# else:
#   statement #2
# ```
# - If the condition is true, execute the first indented statement
# - if the condition is not true, then execute the else indented statements. 
# - Note that Python uses indentation (whitespace) to indicate code sections and scope.
# """
# #example 1: false stmt
# x=3
# y=10
# if x + y == 15:
#     print('true')
# else:
#     print('this stmt is false')

# #example 2: true stmt 
# if x + y == 13:
#     print('True')
# else:
#     print('false')


# # #example 3
# if 10 > 9 : 
#     print('if condition is true.')
# else:
#     print('if condition is false.')


# # #example 4: 3 conditional statement(if/elif/else)

"""if 5 == 7 :
    print('first stmt is true')
elif 2 == 4:
    print('2nd stmt is true')
else:
    print('last stmt it true')



if 10 == 1:
    print('true')
elif 10 == 10:
    print('2nd stmt is true')
else:
    print('these stmts are invalid')

if 5 < 7:
    print('true')
elif 2 > 4:
    print('true')
else:
    print('last stmt is true ')"""

# #in if/else arguements the code will move on to next block once the stmt is fulfilled.
# #meaning if printing an arguement with 2 true statements in a if/elif/else statment, 
# # han python will take the first condition fulfilled and continue on with the code  



# # Let's take an input from the user and grant or deny access accordingly

"""name = input('enter your name.')
if name == 'robbie':
    print('access granted')

name2 = input('enter your name.')
if name2 == 'mohammed':
    print('access granted')
elif name2 == 'robbie':
    print('access granted')
else: 
    print('access denied')"""


# Let's make the code more robust (case insensitive)

"""name = input('enter your name?')
if name == "Ryan" or name == 'RYAN' or name == 'ryan':
    print('access has been granted')
else:
    print('access has been denied ')"""


# """**MINI CHALLENGE #4:**
# - **Write a code that takes a number from the user and indicates if it's positive or negative**
# """

"""num = float(input('enter a number'))
if num > 0:
    print('num is positive')
elif num < 0:
    print('num is negative')
else:
    print('number is zero')"""



#----------------------------------------------
# """**MINI CHALLENGE #5:**
# - **Write a code that takes a number from the user and checks if the number is divisible by 3 but is not a multiple of 7**

"""num2 = int(input('enter a number?'))
if num2%3 == 0 and num2%7!=0:
    print("true")
else:
    print('false')"""
#----------------------------------------------


#----------------------------------------------
# """**MINI CHALLENGE #6:** 
# - **Write a code that takes a number from the user and indicate if the number is even or odd**
# """

"""num3 = int(input('enter a numer'))
if num3%2==0:
    print('even')
else:
    print('odd')"""





#----------------------------------------------

#==========================================================================================================================================================
    
# brands = {
#     "nike": 120,
#     "adidas":100,
#     "puma": 90,
#     "reebok": 75
# }
# name = input('Welcome, what is ur name?')
# money = float(input('what is ur budget?'))
# brand = input("which shoe brand are you interested in? 'nike' for nike, 'adidas' for adidas, 'puma' for puma, 'reebok', for rebook.")

# if brand == 'nike':
#     cost = brands['nike']
#     remainder = money - cost   
# elif brand == 'adidas':
#     cost = brands['adidas']
#     remainder = money - cost  
# elif brand == 'puma':
#     cost = brands['puma']
#     remainder = money - cost   
# elif brand == 'reebok':
#     cost = brands['reebok']
#     remainder = money - cost   
# else:
#     brand = ('na')

# if brand == ('na'):
#     print('currently out of stock.')
# else: 
#     print(f'{name}, you have ${remainder} remaining.')


# if remainder >= brands['adidas'] and remainder > brands['reebok'] == 'nike':
#     choices = brands[1:3]
#     print(f'You can also purchase {choices}.')
# # elif remainder >= brands[2] and remainder > brands[3] == 'adidas':
# #     choices = brands[2:3]
# #     print(f'You can also purchase {choices}.')
# # elif remainder >= brands[2] and remainder > brands[3] == 'puma':
# #     choices = brand[3]
# #     print(f'You can also purchase {choices}.')
# # elif remainder >= brands[2] and remainder > brands[3] == 'rebook':
# #     choices = brands[3]
# else: 
#     print(f'{name}, you can purchase {brand}, you will have ${remainder} remaining. you can also purchase {choices}')
#==========================================================================================================================================================