##Error and Exceptions samples

##sample1
    # try:
    #     for i in ['a','b','c']:
    #         print(i**2)
    # except TypeError:
    #     print("You can't power the string it has to be int")


# ##Sample2
# try:
#     x = 5 
#     y = 0 
#     z = x/y
#     print(z)
# except ZeroDivisionError as e:
#     print("We are having ZeroDivisionError")
# finally:
#     print("All Done")

# ##Sample3
waiting = True
while waiting:
    try:
        square_root = int(input("Enter a number you like to find the square root of: "))
    except:
        print("Enter the correct data type")
        continue
    else:
        # break
        waiting = False
print(square_root ** 2)