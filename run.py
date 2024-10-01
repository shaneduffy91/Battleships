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
            
            if LetterGuess in Choice:
                for index, letter in enumerate(Choice):
                    if letter == LetterGuess:
                        HiddenChoice[index] = LetterGuess
                print("Correct guess!")
                print(GuessedLetters)
            elif LetterGuess in GuessedLetters:
                print("You've already guessed that letter, please choose again!")
                print(GuessedLetters)
            elif not LetterGuess.isalpha():
                print("Invalid input. Please choose a letter.")
                print(GuessedLetters)
            elif len(LetterGuess) != 1:
                print("Please guess a single letter.")
                print(GuessedLetters)
            else:
                Lives -= 1
                print(f"Wrong guess! You have {Lives} lives left.")
                print(GuessedLetters)

            GuessedLetters.append(LetterGuess)
            print(" ".join(HiddenChoice))

            if '_' not in HiddenChoice:
                print("Congratulations! You guessed the word!")
                break
        else:
            print(f"Game over! The word was '{Choice}'.")
        
        PlayAgain = input("Do you want to play again? (Y/N): ").upper()
        if PlayAgain != 'Y':
            print("Thank you for playing Hangman!")
            break

hangman()