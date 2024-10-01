import random

def hangman():

    WordList = ['APOLLO', 'BANANA', 'QUEEN', 'SENTIMENT', 'DOUBLE', 'CIRCLE', 'MENTALITY']

    while True:
        Choice = random.choice(WordList)
        HiddenChoice = ['_'] * len(Choice)
        Lives = 6
        GuessedLetters = []

        print("\nWelcome to Hangman!")
        print(" ".join(HiddenChoice))

        while Lives > 0:
            LetterGuess = input("\nGuess A Letter\n ").upper()
            
            if LetterGuess in GuessedLetters:
                print("You've already guessed that letter.")
            elif LetterGuess in Choice:
                for index, letter in enumerate(Choice):
                    if letter == LetterGuess:
                        HiddenChoice[index] = LetterGuess
                print("Correct guess!")
            elif not LetterGuess.isalpha():
                print("Invalid input. Please choose a letter.")
            elif len(LetterGuess) != 1:
                print("Please guess a single letter.")
            else:
                Lives -= 1
                print(f"Wrong guess! You have {Lives} lives left.")

            GuessedLetters.append(Choice)
            print(" ".join(HiddenChoice))

            if '_' not in HiddenChoice:
                print("Congratulations! You guessed the word!")
                break
        else:
            print(f"Game over! The word was '{Choice}'.")
        
        PlayAgain = input("Do you want to play again? (Y/N): ").upper()
        if PlayAgain != 'Y':
            print("Thanks for playing!")
            break

hangman()