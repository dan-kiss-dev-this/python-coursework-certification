def greet_person(name = 'Rock'):
    '''
    the 3 quotes give info
    :param name: string
    :return: string
    '''
    print('some info')
    print('Hello there, ' + str(name))
    return 'hello there ' + str(name)


z = greet_person(11)  # passing in the name is optional
print(z)

def remainder(num1, num2):
    return num1 % num2

remainder_value = remainder(15, 4)
print(remainder_value)

def my_sum(a,b,c):
    # can only add 3 numbers here
    return a+b+c

def my_sum2(*args):
    return sum(args)

def key_value_func(**kwargs):
    # kwargs is key value pairs
    print(kwargs.get('weight'))


# sum() args and kwrgs
the_sum = sum((1,2,3,4,5))
the_sum2 = my_sum2(1,2,3,4,5)
print(the_sum, the_sum2, my_sum(1,2,3))
key_value_func(name='mike', weight=150, age=27)

age = 27

print(age)

def increase_age():
    # age here is locally scoped
    age = 30
    def add_4_to_age(age):
        age = age + 4
        print('nested method ' +str(age))
    add_4_to_age(age)

increase_age()
print(age)

# Assignment 1:
"""
    Create a function named merge_lists that accepts 2 lists.
    The function is supposed to merge both of those lists together
    and return the result.
"""
def merge_lists(list1, list2):
    return list1 + list2

print(merge_lists([1,2,3], [5,6,7]))

# Assignment 2:
"""
    create a function called separate() that accepts a string as an argument
    and returns a list containing each of the characters of
    the string separated as individual items in the list.
    Make sure to test the function.
"""
def seperate(string):
    return list(string)

print(seperate('hello'))

# Assignment 3:
"""
Create a function called multi_merge that takes a list and a string
as arguments.
The function is supposed to return a merged list
containing the original list argument as well as each of the words that are in
the string argument in addition to each of the characters in the string
argument as individual elements in the list.

"""
def multi_merge(list1, string):
    # a = string.split()
    b = list(string)
    print(string,b)
    print(list1 + b)

multi_merge([1,2,3],'hi')

# Assignment 4:

"""
Define a function called last_list that can accept an unlimited number
of lists but returns only the last list.
Example:
    For example, the below function call should return ['mike', 'john']
    last_list([1,2,3,4,5], ['a', 'b', 'c'], ['mike', 'john'])
"""

def last_list(*args):
    print(args[-1])

last_list([1,2,3,4,5], ['a', 'b', 'c'], ['mike', 'john'])

# Assignment 5:

"""
Define a function called key_list_items that can accept an unlimited number
of lists along with another argument. The function should return
the second_folder to last item in the specific list specified by the user of the function.
Example:
    For example, the below function call should return: jan
    key_list_items("people", things=['book', 'tv'], people=['pete', 'mike', 'jan', 'tom'])
"""

def key_list_items(key, **kwargs):
    list_used = kwargs[key]
    print(list_used[-2])

key_list_items("people", things=['book', 'tv'], people=['pete', 'mike', 'jan', 'tom'])
