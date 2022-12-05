

HANGMAN_ASCII_ART = '''Welcome to the game Hangman
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
    '''

# length_of_word = len(secret_word)
# print(length_of_word*'_ ')
# letter_guessed = input('Guess a letter: ')
# letter_guessed.lower()

def print_start_game(MAX_TRIES):
    print(HANGMAN_ASCII_ART, MAX_TRIES)


def check_valid_input(letter_guessed, old_letters_guessed):
    if len(letter_guessed) > 1 and letter_guessed.isalpha():
        return False
    elif letter_guessed in old_letters_guessed :
        return False

    return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    is_valid = check_valid_input(letter_guessed,old_letters_guessed)
    if is_valid:
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print ('X')
        old_letters_guessed.sort
        print(*old_letters_guessed, sep='->')
        return False

def show_hidden_word(secret_word, old_letters_guessed):
    ans = ["_"] * len(secret_word)
    for i in range(len(old_letters_guessed)):
        for j in range(len(secret_word)):
            if (old_letters_guessed[i] == secret_word[j]):
                ans[j] = secret_word[j]  # If a guessed letter appears in the secret word the '_' will be replaced by this letter
    print(" ".join(ans))  # Print the list with spaces

def check_win(secret_word, old_letters_guessed):
    for i in range(len(secret_word)):
        if secret_word[i] not in old_letters_guessed:
            return False
    return True

def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])

HANGMAN_PHOTOS = {

0:
   " x-------x ",

1:
''' 
     x-------x 
     |
     |
     |
     |
     |
 ''',
2:
    '''
    x-------x
    |       |
    |       0
    |
    |
    |
    ''',
3:
 '''
    x-------x
    |       |
    |       0
    |       |
    |
    |
''',
4:
'''
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
''',
5:
'''
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
''',
6:
'''
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
'''
}

def choose_word(file_path, index):
    file_object = open(file_path)
    file_data = file_object.read()
    words_spllited = file_data.split(" ")
    file_object.close()

    dif_words = len(list(set(words_spllited)))  # how many different words

    the_word = ""
    if ((index - 1) < len(words_spllited)):
        the_word = words_spllited[index - 1]
    while (index - 1) >= len(words_spllited):  # Reaching the index in a circular way
        index = index - len(words_spllited)
        if ((index - 1) < len(words_spllited)):
            the_word = words_spllited[index - 1]
    return the_word.lower()

def main():
    MAX_TRIES = 6 #I have defined it as global variable because the main use it and additional functions use it too
    num_of_tries = 0 # Initialize the number of attempts
    old_letters_guessed = [] # Initialize the list of words guessed by the user
    print_start_game(MAX_TRIES)
    file_path = "C:\\Users\\micha\\Desktop\פייתון\\words.txt"
    # input("Enter file path: ")
    index = int(input("Enter index: "))
    secret_word = choose_word(file_path, index)
    secret_word = secret_word.lower() # lower the letters of the secret word
    print("\nLet’s start!")
    print_hangman(num_of_tries) #initial possition - 0 tries
    show_hidden_word(secret_word, old_letters_guessed) #initial word - only '_' signs
    while (num_of_tries < MAX_TRIES): #As long as the user has not reached the maximum number of attempts - GAME ON
        letter_guessed = input("Guess a letter: ")
        if(try_update_letter_guessed(letter_guessed, old_letters_guessed)): #if the letter is valid
            if(letter_guessed.lower() not in secret_word): #It's considered as "try" only if the letter valid, hasn't been guessed yet and doesn't appear in the secret word
                num_of_tries += 1
                print_hangman(num_of_tries)
                print(old_letters_guessed)
            show_hidden_word(secret_word, old_letters_guessed)
        if(check_win(secret_word, old_letters_guessed)):
            print("\nBRAVO\nYOU WON !!!")
            break
        elif(num_of_tries == MAX_TRIES):
            print("YOU LOSE")
if __name__ == '__main__':
    main()