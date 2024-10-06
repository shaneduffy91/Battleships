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

<!--<a href="https://shaneduffy91.github.io/Hangman/" target="_blank" aria-label="The live project">View the live project here</a>-->

## Features
### Existing Features


<ul>
    <li>Random board generation</li>
        <ul>
        <li>Five ships are randomly placed on the player's board and the computer's board.</li>
        <li>The player cannot see the location of the computer's ships.</li>
        <li>SCREENSHOT</li>
        </ul>
    <li>The player can play against the computer.</li>
    <li>User input is accepted</li>
    <li>Keeps the scores</li>
    <li>SCREENSHOT2</li>
    <li>Input validation and error-checking</li>
        <ul>
        <li>The coordinates entered must be numbers.</li>
        <li>The same coordinates cannot be guessed twice.</li>
        <li>The coordinates entered cannot be outside the size of the grid.</li>
        <li>SCREENSHOT3</li>

## Testing
I have manually tested this project as follows:

- Ran the game in the terminal, played it a few times and fixed a few bugs (see Bugs below).
- Passed the code through the PEP8 linter and resolved a few syntax errors.
- Passed the code through the PEP8 linter a second time and confirmed there are no errors.
- Tested in my local terminal and Code Institute Heroku terminal.


### Bugs
#### Solved Bugs

- When I built the project, I was getting error messages in relation to the naming of the variables.
I renamed all the variables in line with the python naming convention.
- When I tested the game in the terminal, I discovered that the incorrect validation message printed to the terminal when there was an invalid input. This has been resolved.

#### Remaining Bugs

- No bugs remaining on this project.

#### Validator Testing

- Passed the code through the PEP8 linter and no errors returned.

## Credits

- Code Institute for the Heroku Deployment Platform.
- Matt Rudge for his ReadMe example.
- Chris Quinn for his mentoring throughout PP3.
- Wikipedia for the rules of the game.

