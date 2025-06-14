# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

def letter_to_code(letter):
    new_dict = (data[data['letter'] == letter]).to_dict()
    # number_code = new_dict['letter']
    key, value = new_dict.items()
    value = list(value[1].items())[0][1]
    return value

name = input("Enter Name : ").upper()
for letter in name:
    print(letter_to_code(letter))
