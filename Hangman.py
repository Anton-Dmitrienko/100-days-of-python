from wonderwords import RandomWord

HANGMANPICS = [r'''
  +---+
      |
      |
      |
      |
      |
=========''',r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


length_word = int(input("How many letters would you like the word to have: "))
chosen_word = RandomWord().word(word_min_length = length_word, word_max_length = length_word)
word_length = len(chosen_word)

placeholder = "_" * word_length
print(placeholder)

display = placeholder
letter_list = []
attempt = 0
while "_" in display and attempt < 7:
    guess = input("Guess a letter: ").lower()
    if len(guess) == 1:
        if guess in letter_list:
            print(f"You've already tried letter \"{guess}\". Choose another letter")
        elif not guess.isalpha():
            print(f"Special characters are not supported. Choose from the letters")
        else:
            letter_list += guess
            if guess not in chosen_word:
                attempt += 1

        display = ""
        for letter in chosen_word:
            if letter in letter_list:
                display += letter
            else:
                display += "_"
        print(HANGMANPICS[attempt])
        print(f"Tried letters: {letter_list}")
        print(f"Current progress: {display}")

    else:
        print("You cannot try more than 1 letter at a time!\nPlease, try again!")
if not "_" in display:
    print('Congratulations, You won!')
else:
    print(f'Unfortunately, You lost!\n The correct word was: {chosen_word}')
