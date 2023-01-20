import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")


#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}


# Keyword Method with iterrows()
code_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input_word = input("Please type a word: ").upper()

new_list = [code_dict[letter] for letter in input_word]
print(new_list)



