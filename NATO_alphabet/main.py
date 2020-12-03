import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

for (index, row) in df.iterrows():
    dictionary = {row.letter: row.code for (index, row) in df.iterrows()}
print(dictionary)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = input("Your name: ").upper()

output = [values for (keys, values) in dictionary.items() if keys in name]
print(output)
