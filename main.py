import pandas as pd


df = pd.read_csv('nato_phonetic_alphabet.csv')
phonetic_word = {row.letter : row.code for (index, row) in df.iterrows()}

execute = True
while execute:
    word = input("Word: ").upper()
    try:
        output_list = [phonetic_word[letter] for letter in word]
        execute = False
        print(output_list)
    except KeyError:
        print("Sorry, only letter in the alphabet please.")