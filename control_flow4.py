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

