#DataTypes
print()
print('2.Data Types \n')
print('2.1 BOOLEANS')
# Boolean values can be represented as one of two constant objects "False" and "True". 
# Booleans behave like integers 0 and 1.

stockprice1 = 100
stockprice2 = 200
print(stockprice1 > stockprice2)
print(stockprice1 > stockprice2)
print(stockprice1 >= stockprice2)
print(stockprice1 <= stockprice2)
print(stockprice1 == stockprice2)
print(stockprice1 != stockprice2)
print()
"""**MINI CHALLENGE #1:** 
- **What will this code generate?**
```
stock_1_price = 20
stock_2_price = 30
print((stock_1_price < stock_2_price))
print(stock_1_price == stock_2_price)
```
"""
print()
print('2.2. LIST')

# A list is a collection which is ordered and changeable. 
# List allows duplicate members.
# Obtain the datatype
# list with mixed datatypes (for example you can have strings and integers in one list)
# You can have a list inside another list (nested list)
# Access specific elements in the list with Indexing
# Note that the first element in the list has an index of 0 (little confusing but you'll get used to it!)
# indexing for nested lists
mylist1 = ['goog', '5', 'candy', 'cars']
print(mylist1)
mylists2 = ["candy", ['red', 'orange', 'yellow'], ['Porsche', 'mercedes', 'BMW', "Tesla"]]
#print list
print(mylists2)
#access element
print(mylists2[2][3])

# Negative Indexing
mylist3 = [2, 'goog', 5]
print(mylist3[-1])
print(mylist3[-3])
# List Slicing (getting more than one element from a list) 
print(mylists2[2][0:4])
print(mylists2[2][0:2])
# obtain elements starting from index 3 up to and not including element with index 6
robbie= [['Stocks', 'fx', 'options'],['pizza', 'wings', 'burgers'], ['red' ,'blue', 'orange']]
print(robbie[0][1])
# Obtain elements starting from index 3 to end
countries = ['china', 'usa', 'russia', ' india', 'spain', ' japan', 'turkey']
print(countries[2:7])
print(len(countries))
# All elements start to end
  # Obtain the length of the list (how many elements in the list)

"""**MINI CHALLENGE #2:**
- **Print the first, second and last element in the list below**
- **Print all elements in the list, first 3 elements, and last three elements**
```
stocks = ["GOOG", "TSLA", "AAPL", "T", "SP500", "BTC", "EUR/USD"]
```
"""
stocks = ["GOOG", "TSLA", "AAPL", "T", "SP500", "BTC", "EUR/USD"]
print(stocks[0])
print(stocks[1])
print(stocks[6])
print(stocks[:])
print(stocks[0:2])
print(stocks[4:7])

"""**MINI CHALLENGE #3:** 
- **Print GOOG**
- **Print AAPL, GOOG, TSLA** 
- **Print T with two different ways**
```
my_list = ["SP500", ["AAPL", "GOOG", "TSLA"], "BTC", "T"]
```
"""
my_list = ["SP500", ["AAPL", "GOOG", "TSLA"], "BTC", "T"]
print(my_list[1][1])
print(my_list[1][:])
print(my_list[-1])
print(my_list[3])
print()




print('2.3 DICTIONARY')


# my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
# Dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its corresponding value.
# Keys are unique within a dictionary while values may not be. 
# List elements are accessed by their position in the list, via indexing while Dictionary elements are accessed via keys

# Define a dictionary using key-value pairs
# View the dictionary
# Check the data type
# Access specific element in the dictionary using a specific key (ex: Key2)
# Define a dictionary for a bank client listing all his/her assets!
# Access elements in the dictionary
# Add a new item to an existing dictionary
# remove an item from the dictionary
# delete the entire dictionary
# Note that you cannot print it out again because the entire dictionary has been deleted

#BONUS: Nested list in dictionary 
mydict = {'key1' : 'v1',
          'key2' : ['v2', 'v3', 'v4','v5'],
          'key3' : ['v6,' 'v7', 'v8','v9']   
}
print(mydict)
print(type(mydict))
print(mydict['key2'])
key_2 = mydict['key2'] 
print(mydict["key2"][2])
print(f'the actual value of {mydict["key2"][1]} is 2309492384902384230')
print(mydict["key2"][2])


client = {'realestate' : [150000],
          'stock' : [10000],
          'savings' : [20000]
}
print(client)
print(client['stock'])

# add new key value +/ key-value-pair 

client['crypto'] = 5000
print(client['crypto'])
print(client)


#add element to stock 
(client['stock'].append('5 aapl shares'))
print(client['stock'])

#remove + add 
(client['realestate']) = " "
print(client['realestate'])
client['realestate']= (100000)
print(client['realestate'])


#add key value pair with no value 
client['assets']= ""
print(client)
print()
"""**MINI CHALLENGE #4:**
- **Create a dictionary with 3 of your favourite stocks and their prices**
"""


favorite_stock = {'Tesla' : 781,
                 'Amazon' : 3249,
                 'Google' : 2094
}
print(favorite_stock)


print()
print('4. STRINGS')

# A string in Python is a sequence of characters
# String can be enclosed by either double or single quotes


mystring = "hello world"
print(mystring)

# Obtain the datatype
print(type(mystring))

# Combining two strings together (Let's combine the first and last name of a bank's client)
firstname = 'robbie'
lastname = 'hanif '
fullname = firstname + lastname
print(fullname)


# You can combine both strings together and add spaces in between
# to add a space in the name 
fullname = firstname + " " + lastname
print(fullname)

# Methods on strings 
# upper will be used to convert the string into upper case
mystring = ("hello world my name is robbie ")
print(mystring)
uppercase = mystring.upper()
print(uppercase)

# Split us used to divide up the string into words 
wordlist = uppercase.split()

# The output from split is a list
print(wordlist)

# Let's check that the datatype is list!
print(type(wordlist))

# you can index any element in the list using indexing
print(wordlist[2])
print(wordlist[2:6])
# you can specify which letter could be choosed to perform the split

mystring= ('robbiehanif993@gmail.com')
z = mystring.split("@")
print(z)
"""**MINI CHALLENGE #5:**
- **Write a code that takes an input from a bank client asking him/her about their feedback regarding the service. The code should split the client input into words and print them on screen**
"""

#service = input('How was you experience?')
#print(service.split())

        ##service = str(input('did u recieve good service today?'))
        ##split = service.split()
        ##print(f'here is the reponse in a list to determine a market sentiment: {split}')

"""**MINI CHALLENGE #6:**
- **Write a code that prompts a user requesting his/her e-mail and then extracts the user first name (Note that the e-mail is in firstname.lastname@gmail.com**
"""

        ##email = str(input('what is your email address?'))
        ##customername = email.split('.')
        ##print(customername[0])
print()
print('5. TUPLES')

# A tuple is a sequence of immutable Python objects. meaning it cannot be overwritten or changed 
# Tuples are sequences, just like lists. 
# The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.
tuple1 = ('goog', 'nike', 'music', ' ftmo', 'mt4', 3, 6, 9);
tuple2 = (450, 55, 977, 2100)
print(tuple1)
print(tuple2)
print(type(tuple1))

# Accessing elements in a tuple
print(tuple1[4])
print(tuple2[2])

# Tuple slicing
print(tuple1[1:4])

# Changing a vlue of a tuple does not work! 
# 'tuple' object does not support item assignment

# Create a New Tuple from existing Tuples

tuple3 = tuple1 + tuple2
print(tuple3)

"""**MINI CHALLENGE #7:**
- **Define a tuple with your first name, last name, age and the number of stocks in your portfolio. Find the length and type as well.**

"""
tuplename = ('robbie', 'hanif', 28, 0)
print(tuplename)
print(len(tuplename))
print(type(tuplename))

print('6. SETS')
# A set is an unordered collection of items. Every element is unique (no duplicates).
# A set is created by placing all the items (elements) inside curly braces {}, separated by comma or by using the built-in function set().
# set of integers
myset = {'goog', 'aapl', 'tesla'}
print(myset)

myset2 = { 'goog', 'aapl', 'tesla', 't','goog', 'aapl', 'tesla', 't' }
print(myset2)
print(type(myset2))

# set do not have duplicates
"""**MINI CHALLENGE #8:**
- **Remove the duplicates from the following list:**
```
my_list = ['GOOG', 'APPL', 'T','TSLA','T','AAPL', 5, 6,5]
```
"""
my_list = ['GOOG', 'APPL', 'T','TSLA','T','AAPL', 5, 6,5]
out = list(set(my_list))


