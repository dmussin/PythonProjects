# print(7 % 4)
# print(1/2)
# x = "Hello World"
#
# print(x.upper)
#
# a = set([1,1,2,3])
#
# print(a)
#
#

# d = {'k1':{'k2':'hello'}}
# # Grab 'hello'
# print(d['k1']['k2'])



# -----------------
# Getting a little tricker
# d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

#Grab hello

# list = d['k1']
# print(list)
# print(type((list)))
# print(list[0])
# print(list[0]['nest_key'])
# print(type(list[0]['nest_key']))
# print(list[0]['nest_key'][1][0])
# print(type(list[0]['nest_key'][1]))
#
#
# print(d['k1'][0]['nest_key'][1][0])



# ////////////
# This will be hard and annoying!
# d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
#
# print(d['k1'][2]['k2'][1]['tough'][2][0])

# ///////////////////
# index_count = 0
#
# for letter in 'asfjhfhff':
#     print('At index {} the letter is {}'.format(index_count, letter))
#     index_count += 1

#
# index_count = 0
# word = 'asfjhfhff'
#
# for letter in word:
#     print(word[index_count])
#     index_count += 1
#
# for index, letter in enumerate(word):
#     print(index)
#     print(letter)
#     print('\n')
#


# Use for, .split(), and if to create a Statement that will print out words that start with 's':
# st = 'Print only the words that start with s in this sentence'
#
# for _ in st.split():
#     if _[0] == 's':
#         print(_)
#     else:
#         pass


# Use range() to print all the even numbers from 0 to 10.
#
# for num in range(0,11,2):
#     print(num)


# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.


# new_list = [x for x in range(1, 51) if x%3 == 0]
# print(new_list)



# ------------------

# # Go through the string below and if the length of a word is even print "even!"
# st = 'Print every word in this sentence that has an even number of letters'
#
# words = st.split()
#
# for i in words:
#     if len(i) %2 == 0:
#         print(f'even - {i}')


# ------------------
# Write a program that prints the integers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz". For numbers which are multiples of both three
# and five print "FizzBuzz".


# for x in range (1, 101):
#     if x %3 == 0 and x % 5==0:
#         print("FizzBuzz")
#     elif x%3==0:
#         print("Fizz")
#     elif x%5==0:
#         print("Buzz")
#     else:
#         print(x)


# ------------------


# Use List Comprehension to create a list of the first letters of every word in the string below:

# st = 'Create a list of the first letters of every word in this string'
#
# list = [x[0] for x in st.split()]
# print(list)

