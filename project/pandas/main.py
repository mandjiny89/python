import pandas as pd
student_data_frame = pd.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
new_dict = {row.letter:row.code for (index, row) in student_data_frame.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.new_list = []
user_input = input("Enter a string to convert into Phonetics: ").upper()
result = [new_dict[key] for key in user_input]
print(result)


