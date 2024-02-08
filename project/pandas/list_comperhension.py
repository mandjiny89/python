
f = open("file_1.txt", "r")
first_list = f.read().splitlines()

f = open("file_2.txt", "r")
second_list = f.read().splitlines()

result = [int(match) for match in first_list if match in second_list]

# # Write your code above 👆

print(result)