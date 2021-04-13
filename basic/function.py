# def my_function(something):
#     print("my_function is printing " + something)
# my_function("nice")

# def even_number(my_list):
#     for num in my_list:
#         if num % 2 == 0:
#             # print("True")
#             return True
#         else:
#             pass
#     # print("False")    
#     return False

# result = even_number([1,3,5,7])
# print(result)

# Function with *args
# final_list = []
# def my_func(*args):
#     for even in args:
#         if even%2 == 0:
#             final_list.append(even)

# result = my_func(1,2,3,4,5,6,7,8,9,10)
# print (final_list)

# every odd letter should be in lowercase and even letter in uppercase
# def my_func(string):
#     final_word = ''
#     for index in range(len(string)):
#         if(index % 2 == 0):
#             final_word += string[index]
#         else:
#             final_word += string[index].upper()
#     print(final_word)
# my_func("something")

###Warm UP####
##############

# #LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
# def lesser_of_two_evens(a,b):
#     if a%2 == 0 and b%2 == 0:
#         return min(a,b)
#     else:
#         return max(a,b)

# result = lesser_of_two_evens(2,8)
# print(result)

#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# def animal_crackers(text):
#     empty_list = []
#     for string in text.split():
#         empty_list += string[0].lower()
#     if empty_list[0] == empty_list[1]:
#         return True
#     else:
#         return False

# result = animal_crackers('Levelheaded llama')
# print(result)

##MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

# def makes_twenty(n1,n2):
#     if n1 == 20 or n2 == 20 or n1+n2 == 20:
#         return True
#     else:
#         return False

# result = makes_twenty(11,10)
# print(result)

####################
###Level 1 Problems#
####################
# #OLD MACDONALD: Write a function that capitalizes the first and fourth letter of a name
# def old_macdonald(name):
#     first_cut = name[0:3].capitalize()
#     second_cut = name[3:].capitalize()
#     return first_cut+second_cut

# result = old_macdonald("macdonald")
# print(result)

##MASTER YODA: Given a sentence, return a sentence with the words reversed
# def master_yoda(text):
#     word_list = text.split()
#     print(word_list)
#     reverse_list = word_list[:: -1]
#     print(reverse_list)
#     reversed_sentence = " ".join(reverse_list)
#     return reversed_sentence

# result = master_yoda("We are ready")
# print(result)

## ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

# def almost_there(n):
#     if 90 <= n <= 110 or 190 <= n <= 210:
#         return True
#     else:
#         return False

# result = almost_there(195)
# print(result)

####################
###Level 2 Problems#
####################

#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

# def has_33(nums):
#     for index in range(len(nums)-1):
#         if nums[index] == 3 and nums[index+1] == 3:
#             return True
#     else:
#         return False
# result = has_33([1, 3, 1, 2, 3, 4, 3, 3])
# print(result)

## PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# def paper_doll(text):
#     empty_list = [ ]
#     for char in text:
#         empty_list += char*3
#     return "".join(empty_list)

# result = paper_doll("Pondicherry")
# print(result)        



## BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
## blackjack(5,6,7) --> 18
## blackjack(9,9,9) --> 'BUST'
## blackjack(9,9,11) --> 19

# def blackjack(a,b,c):
#     Sum = a + b + c
#     if Sum <= 21:
#         return Sum
#     elif Sum == 21:
#         return ("Black Jack Mate")
#     elif Sum >=22 and 11 in (a,b,c):
#         if Sum - 10 >=22:
#             return "Burst after subtracting"
#         return (Sum - 10)

#     else:
#         return "Burst"

# # blackjack(7,7,7)
# result = blackjack(7,7,7)
# print(result)


##SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
##summer_69([1, 3, 5]) --> 9
##summer_69([4, 5, 6, 7, 8, 9]) --> 9
##summer_69([2, 1, 6, 9, 11]) --> 14

# def summer_69(arr):
#     total = 0
#     add = True
#     for num in arr:
#         while add:
#             if num != 6:
#                 total += num
#                 break
#             else:
#                 return "something wrong"
#     return total


# result = summer_69([4, 5, 6, 7, 8, 9])
# print(result)

## SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
##  spy_game([1,2,4,0,0,7,5]) --> True
##  spy_game([1,0,2,4,0,5,7]) --> True
##  spy_game([1,7,2,0,4,5,0]) --> False

# def spy_game(nums):
#     final_list = [0,0,7,'x']
#     for ind in nums:
#         if ind == final_list[0]:
#             final_list.pop(0)
#     return len(final_list) == 1

# result = spy_game([1,0,4,0,0,5])
# print(result)


##Write a function that computes the volume of a sphere given its radius.
## 4/3*pir**3

# def vol(rad):
#     return float(4/3)*(3.14)*(rad**3)
# result = vol(2)
# print(result)

###Write a function that checks whether a number is in a given range (inclusive of high and low)

# def ran_check(num,low,high):
#     if low < num < high:
#         print(f"{num} is in the range between {low} and {high}")
#         return True
#     else:
#         print(f"{num} is not in the range between {low} and {high}")
#         return False

# # Check
# result = ran_check(3,2,7)
# print(result)

###Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
###Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
###Expected Output : 
###No. of Upper case characters : 4
###No. of Lower case Characters : 33
# def up_low(s):
#     lower_count = []
#     upper_count = []
#     for string in s:
#         if string.isupper():
#             upper_count += [string]
#         elif string.islower():
#             lower_count += [string]
#         else:
#             pass
#     return len(upper_count), "These many upper case" len(lower_count) 

# result = up_low("Hello Mr. Rogers, how are you this fine Tuesday?")
# print(result)


##Write a Python function that takes a list and returns a new list with unique elements of the first list.
##Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
##Unique List : [1, 2, 3, 4, 5]

# def unique_list(lst):
#     return set(lst)

# result = unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
# print(result)

##Write a Python function to multiply all the numbers in a list.
##Sample List : [1, 2, 3, -4]
##Expected Output : -24

# def multiply(numbers):
#     total = 1
#     for multi in numbers:
#         total = total * multi
#     return total

# result = multiply([1, 2, 3, -4])
# print(result)

###Write a Python function that checks whether a word or phrase is palindrome or not.

# def palindrome(s):
#     ss = s.replace(" ", "")
#     print(ss)
#     if ss == ss[::-1]:
#         return True
#     else:
#         return False
# result = palindrome('nurses run')
# print(result)

###Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
##import string

# def ispangram(str1):
#     str1 = str1.replace(' ','')
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     for char in alphabet:
#         if char not in str1.lower():
#             return False
#     return True

# result = ispangram("The quick brown fox jumps over the lazy dog")
# print(result)
