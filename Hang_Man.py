import random
import sys
import os

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()


random_index = random.randint(0, len(words))
guessed_word = []
Exact_word = words[random_index]


tries = 0
count = 0
yes = 0
while tries != 6:
  os.system("cls")
  if count != 0:
    if yes == 0:
        print(f"\nYou Guessed {letter}, that is not in the word, you lost a life")
    print(HANGMANPICS[tries])
  if count == 0:
      count += 1
      print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/       
''')

  
  letter = input("\nGuess a letter : ")
  if letter in Exact_word:
      guessed_word.append(letter)
      yes = 1
  else:
      yes = 0
      tries += 1
  
  for i in Exact_word:
      if i in guessed_word:
          print(i, end = " ")
      else:
          print("_", end = " ")
  if set(guessed_word) == set(Exact_word):
      print("\nYou Win")
      input("\n\n\nPress Enter.....")
      sys.exit()

os.system('cls')
print(HANGMANPICS[-1])
print(f"The word is {Exact_word}")
input("\n\n\nPress Enter.....")