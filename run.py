import random
import os


def clear_screen():
    # Clear the terminal screen based on the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')


def hangman():
    """
    Main game function. Randomly chooses a word from a list of words, displays the word
    as underscores and gives the player 6 lives. The player is asked to guess a letter and then 
    the input is validated. The game continues until the player guesses the word or loses
    all 6 lives. A message is printed to the terminal depending on the result and the player is
    then asked if they would like to play again.
    """

    word_list = ['APOLLO', 'SENTIMENT', 'DOUBLE', 'CIRCLE', 'MENTALITY']

    while True:
        choice = random.choice(word_list)
        hidden_choice = ['_'] * len(choice)
        lives = 6
        guessed_letters = []

        print("\nWelcome to Hangman!\n")
        print(" ".join(hidden_choice))

        while lives > 0:
            letter_guess = input("\nGuess A Letter\n").upper()
            clear_screen()  # Clear the screen after each guess

            if letter_guess in choice:
                for index, letter in enumerate(choice):
                    if letter == letter_guess:
                        hidden_choice[index] = letter_guess
                print("\nCorrect guess!\n")
            elif letter_guess in guessed_letters:
                print("\nLetter already guessed, please choose again!\n")
            elif not letter_guess.isalpha():
                print("\nInvalid input. Please choose a letter.\n")
            elif len(letter_guess) != 1:
                print("\nPlease guess a single letter.\n")
            else:
                lives -= 1
                print(f"\nWrong guess! You have {lives} lives left.\n")

            guessed_letters.append(letter_guess)
            print(" ".join(hidden_choice))

            if '_' not in hidden_choice:
                print("\nCongratulations! You guessed the word!\n")
                break
        else:
            print(f"\nGame over! The word was '{choice}'.\n")

        play_again = input("\nDo you want to play again? (Y/N): \n").upper()
        if play_again != 'Y':
            print("\nThank you for playing Hangman!\n")
            break
        elif play_again == 'Y':
            clear_screen()
            hangman()
            break


hangman()
