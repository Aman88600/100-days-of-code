logo = r"""
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)



keep_going = 'yes'
alphabets = 'abcdefghijklmnopqrstuvwxyz'
print(alphabets.find(''))

def encode(text: str, shift_num: int) -> str:
    cipher = ''
    for i in text:
        pos = alphabets.find(i)
        # Well just checking if it exceeds 26
        if (pos + shift_num) > len(alphabets) - 1:
            cipher_char = str(alphabets[len(alphabets) - (pos + shift_num)])
            cipher += cipher_char
        else:
            cipher += alphabets[pos + shift_num]
    return cipher

def decode(cipher: str, shift_num: int) -> str:
    text = ''
    for i in cipher:
        pos = alphabets.find(i)
        if (pos - shift_num) < 0:
            text_char = alphabets[(len(alphabets) - shift_num)]
            text += text_char
        else:
            text_char = alphabets[pos - shift_num]
            text += text_char
    return text
while keep_going == 'yes':

    coding = input("Type \"encode\" or \"decode\" : ")
    if coding == 'encode':
        text = input('Enter message :').lower()
        shift_num = int(input('Enter shift number : ')) # By default the input() function returns a string
        print(encode(text, shift_num))
    elif coding == 'decode':
        cipher = input('Enter cipher to decode : ').lower()
        shift_num = int(input('Enter shift number : '))
        print(decode(cipher, shift_num))
    keep_going = input("To continue type \"Yes\" and \"No\" to stop : ").lower()
