#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def get_guests_names():
    """Get names from invited_names.txt and append them to a list"""

    guests_names = []
    with open("./Input/Names/invited_names.txt") as guests_file:
        names = guests_file.readlines()
        for name in names:
            guests_names.append(name.strip())
    return guests_names

def replace_names(guest_list):
    """This function replaces the contents of the letter with the guest names"""

    for guests in guest_list:
        with open("./Input/Letters/starting_letter.txt") as letter_file:
            content = letter_file.read()
        content = content.replace("[name]",guests)
        with open(f"./Output/ReadyToSend/{guests}_letter.txt",mode="w") as letter_file:
            letter_file.write(content)


guests_names = get_guests_names()
replace_names(guests_names)
            
