#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []
file = open("Input/Names/invited_names.txt", "r")
text = list(file.read())
file.close()
i = 0
name = ""
while i < len(text):
    if text[i] == '\n':
        names.append(name)
        name = ""
    else:
        name += str(text[i])
    # print(text[i])
    i += 1
names.append(name)
print(names)
file = open("Input/Letters/starting_letter.txt", "r")
whole_letter = []
for i in file.read():
    whole_letter.append(i)
file.close()


def remove_name(text):
    first_pos = 0
    second_pos = 0
    i = 0
    while i < len(text):
        if text[i] == '[':
            first_pos = i
        if text[i] == ']':
            second_pos = i
        i += 1
    del text[first_pos: second_pos + 1]
    return text


for name in names:
    text = ''.join(whole_letter).replace("[name]", name)
    file = open(f"Output/ReadyToSend/{name}.txt", "w")
    file.write(text)
    file.close()
