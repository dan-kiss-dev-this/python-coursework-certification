my_list = [1,4,3,2,5]
my_list2 = [11,14,12]
my_list[0] = 0
my_list.append(8)
my_list.sort()
my_list.reverse()
print(my_list)
sentence1 = 'abcdefg'
print(len(sentence1))
list_size = len(my_list)
print(list_size) # count number of items in list
print(my_list[2:4]) # will have items of position 2 and 3, the 4 is not included
my_list3 = my_list + my_list2
print(my_list3)

my_list4 = ['a', 'b', 'c', 1, 2, 3, ['apple', 'orange', 'banana'], 'd']
my_list4[6][1] = 'pear'
print(my_list4[6][1])

list5 = ['a', 'b', 'c', 'd', 'c']
index_position_list5 = list5.index('c')
count_list5 = list5.count('c')
print(index_position_list5)
print(count_list5)

list6 = [1, 2, 3]
tuple1 = (1,2,3, 'some data', [1, 2, 3])

print(tuple1[1:4])

dictionary1 = { 'k1': 'some data', 'b': 'Kevin'}

dictionary1['b'] = 'Steve'
print(dictionary1)

people_weight_dictionary = {'john': 134, 'michelle': 150, 'mike': 160}
people_weight_dictionary['john'] = 190
people_weight_dictionary.pop('mike')
print(people_weight_dictionary)
# people_weight_dictionary.clear()
print(people_weight_dictionary)
people_weight_dictionary['newDict'] = {'user': 1234, 'user2': 'red'}
print(people_weight_dictionary['newDict']['user'])

print('hello' == 'Hello' or 5 == 5 and 2 != 1)
print(not True)

# Assignment 1:
"""
Print Bill's salary from the my_list object shown below.
my_list = [{'Tom': 20000, 'Bill': 12000}, ['car', 'laptop', 'TV']]
"""
my_list_q1 = [{'Tom': 20000, 'Bill': 12000}, ['car', 'laptop', 'TV']]

print(my_list_q1[0]['Bill'])

# Assignment 2:
"""
Using some of the collection data types we learned about
in the course so such as a list and dictionary, create a
data structure that best represents the following scenario:
Tom has a salary of 20000 and is 22 years old. He owns a few items such as
a jacket, a car, and TV. Mike is another person who makes 24000 and is 27 years old
who owns a bike, a laptop and boat.
"""

tom_and_mike = [
    {'Tom1': {
        'salary': 50000,
        'items': ['jacket', 'car', 'tv']
    }},
    {'Mike1': {'salary': 24000, 'age': 27}}
]

# Assignment 3:
"""
There is a list shown below titled original_list.
Using only what you've learned so far in the course,
write code to create a new list that contains the tuple sorted.
IMPORTANT: you must do this programmatically! Don't just
      hard code a new list with the values rearranged.
"""

original_list = ['cup', 'cereal', 'milk', (8, 4, 3)]
tuple03 = original_list[3][0]
tuple13 = original_list[3][1]
tuple23 = original_list[3][2]
print(tuple13)
sorted_tuple = [tuple03, tuple13, tuple23]
sorted_tuple.sort()
new_tuple = (sorted_tuple[0], sorted_tuple[1], sorted_tuple[2])
original_list[3] = new_tuple
print(original_list)

# Assignment 4:
"""
In the list shown below, replace the letter m with the letter x
and replace the word TV with the word television. Then print my_list.
"""

my_list = [(1, 2), (3, 4), (['c', 'd', 'a', 'm'], [3, 9, 4, 12], 4), 'TV', 42]


my_list[2][0][3] = 'x'
my_list[3] = 'Television'

print(my_list)
