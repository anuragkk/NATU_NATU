import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# new_dict = {row['letter']: row['code'] for index, row in data.iterrows()}

new_dict = {}
for (index, row) in data.iterrows():
    new_dict[row.letter] = row.code
print(new_dict)

while True:
    name = input("Enter a name: \n").upper()

    phonetic_dict = {letter: new_dict[letter] if letter in new_dict else letter for letter in name}
    print(phonetic_dict)
