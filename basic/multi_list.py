fruits = ["apple", "banana", "mango"]
vegs = ['carrot', 'beans', 'potato']
drinks = ['milk', 'water', 'juice']

#Below statements will print user friendly list to choose
print("########################################")
print("Select a fruit from list ", fruits, " or")
print("Select a drink from list ", drinks, " or")
print("Select a veg from list ", vegs)
print("########################################")
user_need = input("What do you like from the above list: ")

# Below what_is_the_item function will retun is the entered item is what list.
def what_is_the_item(item):
    if item in fruits:
        print("User entered " + item + " It's a fruit")
    elif item in drinks:
        print("User entered " + item + " It's a drink")
    elif item in vegs:
        print("User entered " + item + " It's a veg")
    else:
        print("Choose the wrong option from the list")

# Below merge_list function will print all the given list into a single list
def merge_list(*no_of_list):
#    full_list = list1 + list2 + list3
    full_list1 = no_of_list[0] + no_of_list[1] + no_of_list[2]
    print("")
    print("This is printing all given list into a single list: ", full_list1)
    print("")

# Functions will be called in this section
what_is_the_item(user_need)
merge_list(fruits, vegs, drinks)

