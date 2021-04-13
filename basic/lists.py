
#Build this list [0,0,0] two separate ways.
my_list_2 = [0]*3
my_list_4 = [0,0,0]
print(my_list_2, my_list_4)


#Use tow methods indexing for string to call "o"
s = 'hello'
r = s[4]
r1 = s[-1]
print(r,r1)

# Reassing 'Hello' in this nested list to say 'goodbye' instead:
my_list = [1,2,[3,4,'Hello']]
my_list[2][2] = 'Goodbye'
print(my_list)

#Sort this list
list_3 = [3,4,5,2,5,2,9,8]
list_3.sort()
print(list_3)
#Method 2
sorted(list_3)
print(list_3)

