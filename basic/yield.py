# ###Generator used to avoid memory consumption and call the value in order
# ###Example one

# def generate_squares(n):
#     for x in range(n):
#         yield x**2

# something = generate_squares(6)

# print(next(something, "iterate completed")) 
# print(next(something, "iterate completed"))
# print(next(something, "iterate completed"))
# print(next(something, "iterate completed"))
# print(next(something, "iterate completed"))
# print(next(something, "iterate completed"))
# print(next(something, "iterate completed"))### Next is a keyword it can have the next itertable item and the default if the iteratable comes to an end


###Example 2 
# import random

# def rand_num(low,high,n):
#     for i in range(n):
#         yield random.randint(low,high)

# s = rand_num(0,10,2)

# print(next(s, "iterate completed"))

###Example 3

def word_yield(word):
    for i in word:
        yield i

x = word_yield('hello')

print(next(x, "iterate completed"))
print(next(x, "iterate completed"))
print(next(x, "iterate completed"))
print(next(x, "iterate completed"))
print(next(x, "iterate completed"))
print(next(x, "iterate completed"))
