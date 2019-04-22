# A Number Guessing Game

Team Treehouse Python Techdegree Project 1: A Number Guessing Game

## Project Requirements/User Stories

- Make sure your script runs without errors. Catch exceptions and report errors to the user in a meaningful way.
- As a player of the game, I should see a some kind of text header, welcome or game intro message, before or above the menu.
- As a player of the game, I should be continuously prompted for a guess until I get it right.
- As a player of the game, after an incorrect guess I should be told if my answer is higher or lower than the answer, so that I can narrow down my guesses.
- As a player of the game, after the game ends I should be shown my number of attempts at guessing.

### Exceeds Requirements/User Stories

- As a player of the game, my guess should be within the number range. If my guess is outside the guessing range I should be told to try again.
- As a player of the game, after I guess correctly I should be prompted if I would like to play again.
- As a player of the game, at the start of each game I should be shown the current high score (least amount of points), so that I know what I am supposed to beat.

## My Approach

Using the pseudocode given in the Starter File, I went line by line and built each requirement, tested it, then moved on to the next step. I decided to add some time.sleep() calls to give the text some breathing room. I did have to research the list.sort() method to give me a sorted list so that I could display the 'high' score.  A while loop seemed the best to use for the game loop. I used a try block to convert the input string to an int. For the > 10 < 0 check, I felt that if statements were a good fit. I also decided to make invalid guesses count against the player and increment the guess counter. We had a choice to try for Meets Expectations or Exceeds Expecations and for this project, I decided to try for Exceeds.

## What I learned

- Taking project requirements
- Using user stories and pseudocode to break requirements into individual pieces
- Testing each step
- Researching when I get stuck
- Keeping track of changes in Git
- While loops, list sorting, error catching, if statements