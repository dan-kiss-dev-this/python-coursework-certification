print('hello world')
number = 77
print(number)
weight = 150
answer = number + weight
print(answer)

first_name = 'Dan'
last_name = 'Kiss'
print(first_name + ' ' + last_name + ' weights ' + str(weight) + ' lbs')
isFalse = True
print(type('hi'))

number1 = 5
number2 = 2
print(number1 % number2)

sentence = "I'm \n coming home"

print(sentence[0], sentence[-2])
# I and m

sentence2 = 'this is a sentence'
print(sentence2[0:4])
print(sentence2[0:7:2]) #get every second letter starting at 0
print(sentence2[3:]) # get all letters from 3 on
print(sentence2[-2:]) #start from -2 at end and go to real full end
print(sentence2.upper()) # go upper case on self aka on instance of this string
print(sentence2.capitalize()) # cap first letter only
print('234'.isdigit())
print(sentence2.startswith('this'))
print(sentence2.startswith('is', 5)) #does position 5 start with is

sentence3 = 'The sum of 5 + 10 is {0}'.format(50)
print(sentence3)

sentence3 = 'The sum of {0} + {1} is {2}'.format(10, 15, 25) #notice order of args
print(sentence3)

sentence4 = 'abcde'
# sentence4[0] = 'b' # cannot be done
sentence4 = '1' + sentence4[1:]
print(sentence4)

remainder_of_15_div_4 = 15 % 4
print(remainder_of_15_div_4)

print('we have {0} small boxes, {1} large boxes, {2} medium boxes'.format(10,12,12))

# Assignment 3:
"""
    Given 2 variables chars and word, write code to move
    the data contained in the variable word in the exact middle of
    the characters contained in the variable chars and save this
    in a new variable called result and print it.
    NOTE: chars variable will contain only 4 characters
    Example:
    ---------------
    chars = "<<>>"
    word = "hello"
    result - should contain the following string: <<hello>>
"""
chars = '[[]]'
word = 'cool'
result = chars[:2] + word + chars[2:]
print(result)

# Assignment 4:
"""
    Given 2 variables word1 and word2, write code to
    print the concatenation of the 2 words omitting the
    first_folder letter of the string saved in word1 and the second_folder
    letter of the string saved in word2.
    Example:
    ---------------
    word1 = "Vehicle"
    word2 = "Robot"
    result - ehicleRbot
"""
word_section1_assignment4a = 'Computer'
word_section1_assignment4b = 'Truck'

word_section1_assignment4combo = word_section1_assignment4a[1:] + word_section1_assignment4b[0:1] + word_section1_assignment4b[2:]
print(word_section1_assignment4combo)

# Assignment 5:
"""
    Given 2 variables chars and word, write code to move
    the data contained in the variable word in the exact middle of
    the characters contained in the variable chars and save this
    in a new variable called result and print it.
    NOTE: chars variable can contain any even number of characters.
          the len() function can be used to figure out the length of a string
    Example:
    ---------------
    chars = "<[<||>]>"
    word = "mirror"
    result - should contain the following string: <[<|mirror|>]>
"""

chars = "<<[]]]" # this could be a very long string with an even length.
word = "Cool"

# Expected Result Printed: <<[Cool]]]


# Your code below:
print(len(chars))
middle = round(len(chars)/2) #assuming even number given
# note middle below does not include middle number in :middle aka the middle is the cutoff
result5 = chars[:middle] + word + chars[middle:]
print(result5)


