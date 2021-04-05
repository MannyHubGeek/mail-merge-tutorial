PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines() # Turns the names into a list


with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read() # Turns the names into a list
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        print(new_letter)

        with open(f"./Output/ReadyToSend/completed_leter_{stripped_name} .txt", "w") as completed_letter:
            completed_letter.write(new_letter)
