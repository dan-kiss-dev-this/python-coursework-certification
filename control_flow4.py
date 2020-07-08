elephant = 800
hippo = 1400
if elephant < hippo and (3 > 2):
    print('true')
    if 5 < 7:
        print('true again')
else:
    print('false')

animal = 'ape'
if animal == 'cow':
    print('cow eats grass')
elif animal == 'bird':
    print('bird eats seeds')
elif animal == 'monkey' or animal == 'ape':
    print('monkey/ape eats bananas')
else:
    print('not sure what animal eats')

farm_animals = ['goat', 'horse', 'chicken', 'cow', 'dog']

number = 0
for animal in farm_animals:
    sentance = animal + ' is safe in the farm'
    print(number, sentance)
    number += 1

some_string = 'hello'

# character is known as the iteration variable
for character in some_string:
    if character == 'l':
        # break keyword will stop loop execution
        break
    if character == 'h':
        continue
    print(character)

some_list = ['computer', 'car', 'bottle', 'tv']

for item in some_list:
    pass

x = 0
while x < 10:
    print(x)
    x += 2
    # do somehting
else:
    print('done')
    # something else

employees = {'mike': 27000, 'john': 60000, 'rebecca': 65000, 'tom': 30000}

for person in employees.items():
    print(person)

for person_salary in employees.values():
    print(person_salary)

for key, value in employees.items():
    print(key)
    print(value)

employees2 = [('mike', 27000), ('john', 60000), ('rebecca', 65000), ('tom', 30000)]

for element in employees2:
    print(element[0])

word = 'hello'

mylist = list(word)

print(mylist)

for letter in mylist:
    print(letter)

for num in range(2, 10, 3):  # will not include the 10, the 2 is start, 3 is step size
    print(num)

words = ['hello', 'my', 'name', 'is', 'dan']
nums = [1,2,3,4,5]

combinedItems = zip(nums, words)
print(combinedItems)

for item in combinedItems:
    print(item)

for item in enumerate(words):
    print(item)

list_a = ['a','b','c']
list_b = [1,2,3]
list_c = [10,11,12]

zipped_list = list(zip(list_a, list_b, list_c))

print(zipped_list)

for my_tuple in zipped_list:
    print(my_tuple)

for a,b,c in zipped_list:
    print(a)
    print(b)
    print(c)

list_a = ['a','b','c','d']
print('b' in list_a) # will return a boolean value
print('z' in list_a)

print('john' in { 'john': 50})
print(50 in { 'john': 50}.values()) # true we check for value() of 50

print(max(list_a))

from random import randint
random_number = randint(0,1000)
print(random_number)

from random import shuffle
mylist = [1,2,3,4,5]
shuffle(mylist)
print(mylist)

numbers = list(range(100))
print(numbers)
shuffle(numbers)
print(numbers)

# to accept user input and remove blank spaces, int() removes white spaces by default
# note all user input() is taken in as a string
name = input('enter your name: ')
print('hello there ' + name.strip())

# Assignment 1

"""
Create a method called twelver that accepts 2 integer arguments: a and b.
The method should return True if one of the arguments is 12
or if the sum of both arguments equals 12.
twelver(3, 12) → True
twelver(4, 9) → False
twelver(9, 3) → True
"""

def twelver(a,b):
    if a == 12 or b == 12 or (a + b == 12):
        return True
    else:
        return False

print(twelver(12,0),twelver(0,12),twelver(5,7),twelver(4,6))

def twelver2(a,b):
    return (a == 12 or b == 12 or a + b == 12)
print(twelver2(12,0),twelver2(0,12),twelver2(5,7),twelver2(4,6))

# Assignment 2

"""
Create a method called pay_extra that accepts 2 parameters:
 working, and hour. This method will be used to decide whether
 an employee will receive extra pay or not. If an employee is working
 during the hrs of 8pm until 8am in the morning, that means they
 should be paid extra. In that situation the method should return true,
 otherwise it should return false.
 NOTE: the hour parameter should be from 0-23.
        So 8AM is hour 8, and 8PM is hour 20.
Example:
    pay_extra(True, 11) -> false
    pay_extra(False, 5) -> false
    pay_extra(True, 6)  -> true
"""
def pay_extra(start, end):
    if start < 8 or 20 < end:
        return True
    return False

print(pay_extra(6,16))
print(pay_extra(9,20))
print(pay_extra(12,22))

# Assignment 3

"""
Given a list of ints, return True if the sequence of numbers 1, 2, 3
appears in the list anywhere, false otherwise.
sequence([1, 1, 2, 3, 1]) → True
sequence([1, 1, 2, 4, 1]) → False
sequence([1, 1, 2, 1, 2, 3]) → True
sequence([1, 2]) → False
sequence([]) → False
"""

def sequence(arr):
    for i in range(len(arr)-2):
        #see if 1,2,3 exists in the array
        if arr[i] == 1 and arr[i+1] == 2 and arr[i+2] == 3:
            return True
    return False

print(sequence([1, 1, 2, 3, 1]))

# Assignment 4

"""
Given a non-empty string like "Code" return a string like "CCoCodCode".
grow_string('Code') → 'CCoCodCode'
grow_string('abc') → 'aababc'
grow_string('ab') → 'aab'
"""

def grow_string(str):
    result = ''
    for i in range(len(str)):
        result = result + str[:i + 1]
    return result

print(grow_string('code'))

"""
Define a method that accepts a list as an argument
and returns True if one of the first_folder 4 elements
in the list is a 6. The list length may be less than 4.
first3([1, 2, 6, 3, 4]) → True
first3([1, 2, 3, 4, 6]) → False
first3([1, 2, 3, 4, 5]) → False
"""

def first4(arr):
    if arr[0] == 6 or arr[1] == 6 or arr[2] == 6 or arr[3] == 6:
        return True
    return False

print(first4([1, 2, 1, 3, 6]))

# Assignment 6

"""
Create a function called last2 that accepts a string argument.
The function should return the count of the number of times that the last
2 characters appear in the rest of the string. You should not count
the last 2 characters as an occurrence. The last 2 characters is just the
sequence your function should look for in the remaining string.
So "hixxxhi" yields 1 (we won't count the end substring).
last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
"""
def last2(str):
    if len(str) <= 2:
        return 0
    last2 = str[len(str) - 2:]
    count = 0

    for i in range(len(str) -2 ):
        sub = str[i : i + 2]
        if sub == last2:
            count = count + 1
    return count

print(last2('axxxaaxx'))

# Assignment 7
"""
Given 2 strings, a and b, return the number of the positions where
they contain the same length 2 substring. So "xxcaazz" and "xxbaaz"
yields 3, since the "xx", "aa", and "az" substrings appear in the same
place in both strings.
EXAMPLE:
    string_match('xxcaazz', 'xxbaaz') → 3
    string_match('abc', 'abc') → 2
    string_match('abc', 'axc') → 0
"""

def string_match(a, b):
    #figure out which string is shorter
    shorter = min(len(a), len(b))

    count = 0

    for i in range(shorter - 1):
        a_sub = a[i : i + 2] # gives substring of size 2
        b_sub = b[i : i + 2]
        if a_sub == b_sub:
            count = count + 1
    return count

print(string_match('xxcaazz', 'xxbaaz'))

# Assignment 8

"""
Return the sum of the numbers in the list, except ignore sections of
numbers starting with a 7 and extending to the next 8
(every 7 will be followed by at least one 8).
Return 0 for no numbers.
EXAMPLE:
sum78([1, 2, 2]) → 5
sum78([1, 2, 2, 7, 99, 99, 8]) → 5
sum78([1, 1, 7, 8, 2]) → 4
"""

def sum78(nums):
    sum = 0
    in_range = False

    for i in range(len(nums)):
        if nums[i] == 7:
            in_range = True
        if in_range == False:
            sum += nums[i]
        if nums[i] == 8:
            in_range = False

    return sum

print(sum78([1, 2, 2, 7, 99, 99, 8,4]))

# Assignment 9

"""
We have 2 variables. fr and d. fr is a list of strings and d is a dictionary with email
addresses as keys and numbers as values (numbers in string format).
Write code to replace the email address in each of the strings in the fr list with
the associated value of that email looked up from the dictionary d.
If the dictionary does not contain the email found in the list, add a new entry
in the dictionary for the email found in the fr list. The value for this new email key
will be the next highest value number in the dictionary in string format.
Once the dictionary is populated with this new email key and a new number value,
replace that email's occurrence in the fr list with the number value.
The output of running your completed code should be the following:
Value of fr:
['199|4|11|GDSPV', '199|16|82|GDSPV', '205|12|82|GDSPV', '206|19|82|GDSPV']
Value of d:
{'7@comp1.COM': '199', '8@comp4.COM': '200', '13@comp1.COM': '205', '26@comp1.COM': '206'}
"""
