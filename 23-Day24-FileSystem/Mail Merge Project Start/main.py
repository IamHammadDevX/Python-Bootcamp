PLACEHOLDER = "[name]"


with open(".\\Input\\Names\\invited_names.txt") as names_file:
    names_content = names_file.readlines()
    


with open(".\\Input\\Letters\\starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names_content:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f".\\Output\\ReadyToSend\\letter_for_{stripped_name}.txt", mode="w") as letter:    
            letter.write(new_letter)


    

