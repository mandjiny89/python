item = input("Enter either aplha or number: ")

def machine1(item):
    a = item.isalpha()
    b = item.isnumeric()
    c = item.isalnum()
    d = item
    print(d)
    if a == True:
        print("it's Alpha")
    elif b == True:
        print("it's Numeric")
    elif c == True:
        print("This is alphanum")
    elif isinstance(dict(d),dict):
        print("it's a list type")
    else:
        print("it's not a valid data")

machine1(item)

# import json

# d = '{"key": "value1", "key_2": "value_2"}'
# e = json.loads(d)
# f = json.dumps(e)
# if isinstance(f,str):
#     print("correct")