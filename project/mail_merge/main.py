#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


# class Mailmerge():
#     def __init__(self):


name_list = []
with open("./Input/Names/invited_names.txt") as i:
    for i_name in i.readlines():
        i_name = i_name.strip()
        name_list.append(i_name)

with open("./Input/Letters/starting_letter.txt", "r") as l:
    to_replace = l.read()
    for name in name_list:
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as final:
                after_replacing = to_replace.replace("[name]", name)
                final.write(after_replacing)





# print(name_list)

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp