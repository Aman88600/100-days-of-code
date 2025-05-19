from random import randint
hangman_logo =r"""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
"""

hangman_lives = [
r"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
"""
,
r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
"""
,
r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
r"""
"""
]
print(hangman_logo)
words = [
    "apple", "banana", "puzzle", "guitar", "winter", "oxygen", "pirate", "island", "dragon", "castle",
    "ninja", "monster", "wizard", "rocket", "jungle", "planet", "thunder", "forest", "vampire", "robot",
    "mirror", "whisper", "galaxy", "volcano", "diamond", "shadow", "blanket", "magnet", "bubble", "secret",
    "cobra", "bridge", "candle", "cookie", "feather", "helmet", "igloo", "leopard", "mermaid", "notebook",
    "orbit", "quartz", "rainbow", "skeleton", "tornado", "unicorn", "velvet", "whirlpool", "xenon", "zombie"
]

def convert_word_to_dash(word: str, right_guesses: list) -> str:
    dashed_string = ''
    for i in word:
        if i in right_guesses:
            dashed_string += i
        else:
            dashed_string += '_' 
    return dashed_string

unique_word = []

random_num = randint(0, len(words) - 1)
word = words[random_num]
for i in words[random_num]:
    if i not in unique_word:
        unique_word.append(i)
lives = 6
user_guesses = []
right_guesses = []
while lives > 0:
    print(hangman_lives[6 - lives])
    print(f"word to guess {convert_word_to_dash(word, right_guesses)}")
    if len(right_guesses) == len(unique_word):
        print("You Win!")
        break
    user_guess = input('Enter Your Guess: ')
    if (user_guess in user_guesses) or (len(user_guess) == 0):
        print("You already guessed that")
    elif user_guess in unique_word:
        user_guesses.append(user_guess)
        right_guesses.append(user_guess)
    else:
        user_guesses.append(user_guess)
        print(f"Your Guess {user_guess} is not in word")
        lives -= 1
    print(f"You Got {lives} left")


if lives == 0:
    print(f'The word was {word}')
    