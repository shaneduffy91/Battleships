# Project 3 - Hangman

For my third project with Code Institute, I have created a Hangman game.

## Rules of the Game
* Hangman is a guessing game for two or more players or one player vs the computer. For more information 
see Wikipedia.

* In this version of the game, the player enters their name and the computer randomly generates a word and 
displays it as a row of underscores representing each letter in the word.

* The word randomly generated by the computer must not be a proper noun. In this version of the 
game, the computer randomly selects a word from a list of improper nouns.

* The player has to guess the word by guessing one letter on each turn.

* If the letter guessed is in the word, the computer will reveal all instances of this letter in place of the underscores.

* The player has 6 lives and if an incorrect guess is made, the player will lose a life.

* If all the letters of the word are guessed correctly, the player wins the game.

* If the player fails to guess all the letters in the word and all lives are lost, then the game is over and the word in revealed to the player. 

* The player then has a choice if they would like to play again.

* View the live project here (https://shaneduffy91.github.io/Hangman/).

## Features
### Existing Features

* Random word selection from computer
    - The computer randomly selects a word from a list of improper nouns
    - The word is displayed as underscores 
    - Player tries to guess the word by guessing the letters in the word 

    ![Screenshot of Welcome to Hangman.](https://github.com/shaneduffy91/Hangman/blob/main/welcomeToHangman.png)

* Play against the computer
* Accepts player input
* Validates input and checks for errors
    - You must choose a letter
    - You cannot guess the same letter twice
    - You cannot guess more than one letter at one time

![Screenshot of single letter validation.](https://github.com/shaneduffy91/Hangman/blob/main/singleLetter.png)

![Screenshot of invalid input.](https://github.com/shaneduffy91/Hangman/blob/main/invalidInput.png)

* Displays how many lives the player has left, when an incorrect guess is made.

![Screenshot of wrong guess.](https://github.com/shaneduffy91/Hangman/blob/main/wrongGuess.png)

## Testing
I have manually tested this project as follows:

* Ran the game in the terminal, played it a few times and fixed a few bugs (see Bugs below).
* Passed the code through the PEP8 linter and resolved a few syntax errors.
* Passed the code through the PEP8 linter a second time and confirmed there are no errors.
* Tested in my local terminal and Code Institute Heroku terminal.


### Bugs
#### Solved Bugs

* When I built the project, I was getting error messages in relation to the naming of the variables.
I renamed all the variables in line with the python naming convention.
* When I tested the game in the terminal, I discovered that the incorrect validation message printed to the terminal when there was an invalid input. This has been resolved.

#### Remaining Bugs

* No bugs remaining on this project.

#### Validator Testing

* Passed the code through the PEP8 linter and no errors returned.
![Screenshot of the PEP8 linter wih no errors returned.](https://github.com/shaneduffy91/Hangman/blob/main/PP3-linter.png)

## Deployment
This project was deployed using the Code Institute mock terminal for Heroku, as follows:

* Fork or clone this repository on Github
* Create a new Heroku app
* Set the first buildback to Python
* Set the second buildback to Node.js
* Link the Heroku app to the repository
* Click on Deploy

## Credits

* Code Institute for the Heroku Deployment Platform.
* Matt Rudge for his ReadMe example.
* Chris Quinn for his mentoring throughout PP3.
* Wikipedia for the rules of the game.

