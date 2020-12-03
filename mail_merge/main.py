# TODO: Create a letter using starting_letter.docx
with open("./Input/Letters/starting_letter.docx", mode='r') as lr:
    letters = lr.readlines()
with open("./Input/Names/invited_names.txt", mode='r') as name_list:
    names = name_list.readlines()
for name in names:
    name = name.strip()
    with open(f"./Output/ReadyToSend/{name}.docx", mode="w") as lw:
        for n in names:
            letters[0] = letters[0].replace("[name]", n)
        for line in letters:
            lw.write(line)

# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
