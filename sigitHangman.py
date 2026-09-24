# ==========================================
# constants and definitions
# ==========================================

HANGMAN_PHOTOS = {
    1: r"""    x-------x""",

    2: r"""    x-------x
    |
    |
    |
    |
    |""",

    3: r"""    x-------x
    |       |
    |       0
    |
    |
    |""",

    4: r"""    x-------x
    |       |
    |       0
    |       |
    |
    |""",

    5: r"""    x-------x
    |       |
    |       0
    |      /|\
    |
    |""",

    6: r"""    x-------x
    |       |
    |       0
    |      /|\
    |      /
    |""",

    7: r"""    x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |"""
}

# ==========================================
# helper functions
# ==========================================

def print_start_screen():
    HANGMAN_ASCII_ART = "Welcome to the game Hangman" + "\n" + r"""      
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/ """
    MAX_TRIES = 6
    print(HANGMAN_ASCII_ART + "\n", MAX_TRIES)


def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])


def choose_word(file_path, index):
    with open(file_path, 'r') as source_file:
        content = source_file.read()

    words = content.split()
    unique_words_count = len(set(words))

    chosen_word = words[(index - 1) % len(words)]

    return chosen_word


def check_valid_input(player_guess, old_letters_guessed):
    return len(player_guess) == 1 and player_guess.isalpha() and player_guess not in old_letters_guessed


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    letter_guessed = letter_guessed.lower()
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    print("X")
    old_letters_guessed[:] = [letter.lower() for letter in old_letters_guessed]
    sorted_letters = sorted(old_letters_guessed)
    print(" -> ".join(sorted_letters))
    return False


def show_hidden_word(secret_word, old_letters_guessed):
    result = []
    for letter in secret_word:
        if letter in old_letters_guessed:
            result.append(letter)
        else:
            result.append("_")
    return " ".join(result)


def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True

# ==========================================
# main
# ==========================================

def main():
    print_start_screen()
    secret_word = choose_word(input("Enter file path: "), int(input("Enter word index: ")))
    num_of_tries = 0
    old_letters_guessed = []
    print_hangman(num_of_tries + 1)

    while num_of_tries < 6 and not check_win(secret_word, old_letters_guessed):
        print(show_hidden_word(secret_word, old_letters_guessed))
        char = input("Guess a letter: ")

        if try_update_letter_guessed(char, old_letters_guessed):
            if char.lower() not in secret_word:
                num_of_tries += 1
                print(":(")
                print_hangman(num_of_tries + 1)
    print(show_hidden_word(secret_word, old_letters_guessed))
    if check_win(secret_word, old_letters_guessed):
        print("WIN")
    else:
        print("LOSE")

if __name__ == "__main__":
    main()