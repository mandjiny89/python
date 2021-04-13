# #Use for, .split(), and if to create a Statement that will print out words that start with 's':
# st = 'Print only the words that start with s in this sentence'
# new_st = st.split()
# for s in new_st:
#     if s.startswith("s"):
#         print(s)
# print('\n Next code running')

# # Use range() to print all the even numbers from 0 to 10.

# # range_even = range(10)
# for item in range(0,11,2):
#         print(item)
# print('\n Next code running')

# # Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
# result = [item for item in range(50) if item % 3 == 0]
# print(result, '\n')
# print('\n Next code running')

# #Go through the string below and if the length of a word is even print "even!"
# st = 'Print every word in this sentence that has an even number of letters'
# for item in st.split():
#     if len(item) % 2 == 0:
#         print(item)
# print('\n Next code running')


# #Write a program that prints the integers from 1 to 100. 
# #But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". 
# #For numbers which are multiples of both three and five print "FizzBuzz".
# for item in range(100):
#     if item % 3 == 0 and item % 5 == 0:
#         print("FizzBuzz")
#     elif item % 3 == 0:
#         print("Fuzz")
#     elif item % 5 == 0:
#         print("Buzz")
#     else:
#         print(item)

# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
newlist = [x[0] for x in st.split()]
print(newlist)
