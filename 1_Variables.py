

# 1. VARIABLES ASSIGNMENT
"""
print()
# Define a variable named "portfolio_1" and assign a number (integer) to it
portfolio_1 = 5000
# Let's view "portfolio_1"
print(portfolio_1)
# Define a variable named "portfolio_2" and assign a number (float) to it
portfolio_2 = 5000.5
# Let's view "portfolio_2"
print(portfolio_2)
# Let's overwrite "portfolio_2" (assume your portfolio value increased)
portfolio_2 = 3000.5
print(portfolio_2)
print()
        # overwriting a value of a variable will print the most recent entry 
# Get the type of "portfolio_1" which is integer
# integer is a whole number (no decimals) that could be positive or negative
print(type(portfolio_1))
# Get the type of "portfolio_2" which is float
# Float are real numbers with a decimal point dividing the integer and fractional parts
print(type(portfolio_2))
print()

"""**MINI CHALLENGE #1:**
- **We defined a variable AMZN (Ticker symbol for Amazon stock) and we assigned these 3 values listed below to it. Without executing any code cells, what will these lines of code generate?**
- **Verify your answer by executing the code cells**"""

AMZN = 3324
AMZN = 3400
AMZN = 3530
print(AMZN)

"""**MINI CHALLENGE #2:**
- **We defined a variable AAPL (Ticker symbol for Apple stock) and we assigned these 2 values listed below to it. Without executing any code cells, what will these lines of code generate?**
- **Verify your answer by executing the code cells** """

AAPL = 112
AAPL = 115.3
print(type(AAPL))
print()

"""# 2. MATH OPERATIONS"""

# Define a variable named AAPL and initialize it with 5 indicating that we own 5 stocks
# Let's assume that we bought an additional stock so now we have 6 stocks instead of 5 
# We can increment AAPL by 1 stock as follows:
AAPL = 5 
AAPL = AAPL + 1
print(AAPL)
print()
# Alternatively, we can increment the variable AAPL by 1 as follows:
AAPL = 5 
AAPL+=14
print(AAPL)
# Let's assume that the price of AAPL stock is $260 and we currently have 5 AAPL stocks in our portfolio
# We can calculate the total portfolio value (account balance) as follows:
AAPL_count = 5 
AAPL_price = 260
AB = AAPL_count * AAPL_price
print(AB)
print()

# Let's assume you have $20000 USD in our account
# We want to buy AMZN stocks using the total amount 
# AMZN stock is priced at $3116 each
# Divide the account balance by Amazon stock price and place the answer in units

AMZN = 3116
account = 20000
shares = account/AMZN
print(shares)
print()

"""**MINI CHALLENGE #3:** 
- **Write a code that calculates the total value of a portfolio assuming that you own 15 Google stocks (Sticker Symbol: GOOG) priced at 1500 each** 
"""
goog = 1500
os = 15 
total = goog * os
print(total)


"""**MINI CHALLENGE #4:**
- **Write a code that takes in Google (GOOG) stock prices at two days and calculate the return:**
  - **GOOG price on day 1 = \$260** 
  - **GOOG price on day 2 = \$280**"""

goog1 = 260
goog2 = 280 
price_difference = goog2 - goog1 
percentgain = (price_difference / goog1) * 100
print(percentgain)
print()

"""# 3. ORDER OF OPERATIONS (PRECEDENCE)"""
# add 3 and 4 and then multiply the answer by 5
# Note that parantheses have the highest precedence
# Multiplication has higher precedence compared to addition
# Division has higher precedence compared to addition"""

total1 = 3 + 4 * 5
print(total1)
total2 = (3 + 4) * 5
print(total2)
"""**MINI CHALLENGE #5:**
- **Assume that you own 15 shares of AAPL stock priced at \$150 a share. Apple announced the launch of 5 new products with exceptional features so the stock price increased to $170 a share. Calculate the total profit.**"""


shares=15
cost=150
cost2=170
value = shares*cost 
profits = (cost2 * shares) - value 
print(profits)

"""**MINI CHALLENGE #6:** 
- **Write a code that performs the following mathematical operation: z = |x − y| * (x + y)**
"""
x=10
y=8
z = abs(x-y) *(x+y)
print(z)
# |x-y| = absolute value of integers subtracted  (straight lines)
print()

"""# 4. PRINT OPERATION"""

# Print function is used to print elements on the screen
# Define a string x 
# A string in Python is a sequence of characters
# String in python are surrounded by single or double quotation marks
x = 'was good'
print(x)
# Obtain the data type for 'x'
# Print x
print(type(x))


# Define a string and put 'Apple Inc.' in it

company='Apple Inc.'
print(f"ticker name for {company} is 'AAPL'.")
print()

# The format() method formats the specified value and insert it in the placeholder. 
# The placeholder is defined using curly braces: {}

#two methods to plug in varibles in a string statement 
# You can place two or more placeholders with print function
color1 = ('Red')
color2 = ('Blue')
print(f'My favorite colors are {color1} and {color2}.')

#or

shares= 30 
print('I own {} shares of {}'.format(shares,company))
print()

#using this method will require to know the specifc variables for each placeholder. 
#two methods to plug in varibles in a string statement 


"""**MINI CHALLENGE #7:**
- **Write a code that print out the above statement along with AAPL ticker**
- **i.e.: I own 30 shares of Apple Inc.(AAPL)** 
"""
ticker = ('(FB)')
stock = ('Facebook')
shares_owned = ('30')
print('I own {} shares of {} {}.'.format(shares_owned,stock,ticker))
#or
print(f'I own {shares_owned} shares of {stock} {ticker}.')


"""# 5. GET USER INPUT"""

# input is a built-in function in python
# Get bank client name as an input and print it out on the screen
name = input('Wlecome, What is your name?')
print(name)
# Obtain bank client data such as name, age and assets and print them all out on the screen
print(name)
age = input('How old are you?')
print(age)
networth = input('What is your total net worth? (Assets-Laibilities)')
print(networth)
print(f'My name is {name}, I am {age} years old, and my estimated net worth is ${networth}.') 
# Obtain user inputs, perform mathematical operation, and print the results 
# Note: Are you getting an error? Move to the next code cell
# Convert from string datatype to integer datatype prior to performing addition
x = input('Please enter the price of Apple stock today?')
y = input('Enter the # of Apple stocks you want to buy.')
print(f'Total funds to required to buy {y} Apple stock is ${int(x)*int(y)} at the current price of ${x} per share.')

"""**MINI CHALLENGE #8:** 
- **Write a code that takes in the name of the stock, price at which it is selling, the number of stocks that you want to own and prints out the total funds required to buy this stock. Find a sample expected output below:**

  - Enter the price of the stock you want to buy: 3000  
  - Enter the number of stocks that you want to buy: 5
  - Enter the name of the stock that you want to buy: AMZN
  - The total funds required to buy 5 number of AMZN stocks at 3000 is 15000"""

price_of_stock= input('Enter the price of the stock you want to buy.')
num_of_stocks= input('How many stocks would you like to purchase?')
name_of_stock= input('What is the stock you will invest in?')

print(f'The total required funds to purchase {num_of_stocks} shares of {name_of_stock} is ${int(price_of_stock) * int(num_of_stocks)} at the current price of ${price_of_stock} per share.')








