import random

def hangman():

    word_list = ['APOLLO', 'BANANA', 'QUEEN', 'SENTIMENT', 'DOUBLE', 'CIRCLE', 'MENTALITY']

    while True:
        choice = random.choice(word_list)
        hidden_choice = ['_'] * len(choice)
        lives = 6
        guessed_letters = []

        print("\nWelcome to Hangman!")
        print(" ".join(hidden_choice))

        while lives > 0:
            letter_guess = input("\nGuess A Letter\n ").upper()
            
            if letter_guess in choice:
                for index, letter in enumerate(choice):
                    if letter == letter_guess:
                        hidden_choice[index] = letter_guess
                print("Correct guess!")
                #print(guessed_letters)
            elif letter_guess in guessed_letters:
                print("You've already guessed that letter, please choose again!")
                #print(guessed_letters)
            elif not letter_guess.isalpha():
                print("Invalid input. Please choose a letter.")
                #print(guessed_letters)
            elif len(letter_guess) != 1:
                print("Please guess a single letter.")
                #print(guessed_letters)
            else:
                lives -= 1
                print(f"Wrong guess! You have {lives} lives left.")
                #print(guessed_letters)

            guessed_letters.append(letter_guess)
            print(" ".join(hidden_choice))

            if '_' not in hidden_choice:
                print("Congratulations! You guessed the word!")
                break
        else:
            print(f"Game over! The word was '{choice}'.")
        
        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again != 'Y':
            print("Thank you for playing Hangman!")
            break

hangman()