![Game on different devices](/images/amIresponive.png)

Here is a live link to the game [Try it](https://blackjack-by-ciaran-conway.herokuapp.com/)

Here is a link to my repository [here](https://github.com/ConwayC1987/BlackJack)
***

# BLACKJACK

This is terminal based game of the classic casino card game, Blackjack, using Python. The runs in the Code Institute mock terimal using Heroku. The game allows a player to play against a computer dealer and follow the standard rules of Blackjack.
***

## Pre-planning

A workflow model was needed for the project and I decided to us Lucid chart to help plan the project out. The flow chart was made using https://www.lucidchart.com/pages/. I decided that I would use colour in the project and decided to use easy to see colours like green, red and some blue. I wanted to add colour to the cards suits also.

![Game flow chart](/images/flowchart.png)
***

## Structure of the code

1. Deck: Make a deck of cards and join the suits and ranks together. Add random module to be able to shuffle the cards, add a function that will deal the top card  on the deck.
2. Betting: Before the hand is seen the player is asked to make a bet. They start with 100 chips and every win or loss will affect their chip count.
3. Card: Make cards using ASSCI art and make the hearts and diamonds red and the rest black. Make a separte card for the dealer for the hidden card. Print the dealers cards on the top in a row and the player cards underneath them in a row. 
4. Calculate: Calculate the value of the players cards and the dealer cards. If their is an ace and the player is over 21 then the ace's value becomes 1. Check the player hand for blackjack and check the dealers cards for blackjack after the player decides to stand.
5. Game play: Game starts user is asked to make a bet, then card are shown, the user is then asked to hit or stand until they decide to stand, then the dealers cards will be shown and a winner is decided. The winner is who is closest to 21 without going over it. 
***

## Game Rules

1. Aim of JackJack is to get 21 or as close to as possible.
2. Jacks, kings and queens are worth 10. 
3. Ace can be either 1 or 11.
4. You get 2 cards showing dealer will recieve 1 card face down.
5. Choice is to hit or stand until you or the dealer goes bust.
6. You will start with 100 chips and can bet each hand.
7. You will be playing against the computer
***

## Game Flow

When the game starts, the game title is displayed and it ask's the player what their name is.

![Greeting page](/images/greeting_pg.png)

When the player types in their name, they get a greeting message and the game options are displayed.

![Option page](/images/options_pg.png)

If the player wants to read the rules the screen is cleared and the rules are shown to the player with the game options underneath.

![Game rules page](/images/rules_pg.png)

If the player selects 1 then the game will start and the player will be asked to make a bet.

![Make a bet](/images/place_bet.png)

After the player makes a bet the cards will print to the screen and the player will have a choice to hit or stand.

![Cards being displayed on the screen](/images/game_starts.png)

The game will play until either the player goes bust or decides to stand and a winner is determined on who is closest to 21. The game will end if the players chips run out.

![Cards being displayed on the screen](/images/dealer_bust.png)


If the user selects 3 in the options the program will stop.

***

## Features left to implement

I would like to add an option to be add more player's to the game. If I had more time I would add a higest score page and the maybe a method to record the player's win/loss ratio and their winning to it. Also there is a few different aspects of a game of blackjack I wanted to add but I didn't have time, like a way to split the players and make an extra bet.   

***

## Technologies used

1. Gitpod was used to write the code and test it.
2. Github was used to save the project and store it.
3. Python was the coding language used to make the project.
4. Heroku was used to deploy the project giving a live moblie link to the project.

***

## Testing

| Test                       | Results |
| -------------------------- | ------- |
| Game title displaying      |  Pass   |
| -------------------------- |---------|
| Ask player for their name  | Pass    |
| -------------------------- |---------|
| User gets welcome message  | Pass    |
| and options                |         |
| -------------------------- |---------|
| If user selects 1 the game | Pass    |
| starts                     |         |
| -------------------------- |---------|
| When the player bets       | Pass    |
| and game starts            |         |
| -------------------------- |---------|
| If the player decides to   | Pass    |
| hit new cards shows        |         |
| -------------------------- |---------|
| If the player decides to   | Pass    |
| stand, dealer cards are    |         |
| shown                      |         |
| -------------------------- |---------|
| Calculate the value of the | Pass    |
| hand to find the winner,   |         |
| check for blackjack        |         |
| -------------------------- |---------|
| Chips minus the total if   | Pass    |
| player loses and adds if   |         |
| they win                   |         |
| -------------------------- |---------|
| Press 2 open the rules     | Pass    |
| -------------------------- |---------|
| Press 3 the program stops  | Pass    |
| -------------------------- |---------|
***

## Bugs
There is a bug in the code that for some reason 10 are being displayed on the terminal as 1 instead of 10. 
- At the start I thought it was aces that were showing as 1 but eventualy it was discovered it was the 10 that was causing the problem. I think the reason for the error is 10 was an extra digit to the rest of cards and when I split the ranks and suits to draw a card using assci art it is being split at 1 and 0 rather than being split at 10 and then the suit. This took over 7 days to discover what card it was happening with and as to why it might be happening. I decided to rewrite the code using a new approach to fix the error.

- Another bug was when the dealer got blackjack it wasn't showing any of the players cards. This was also fixed.

- A bug that could break the code was I wasn't checking if the user was using a positive number when betting, this was also fixed.

- A lot of small and big bugs were found and all fixed to the best of my knowledge with the project.
***

## Remaining bugs

- All known bugs fixed.
***

## Validator Report

The code was ran through the https://pep8ci.herokuapp.com/ to test for errors but the only errors was lines of code that were too long in lenght but everything fits on the screen.

![Validator report](/images/linter_result.png)
***

## Deployment
1. Navigate to heroku.com & log in.

2. Click "new" and create a new App.

3. Give the application a name and then choose your region and Click "Create app".

4. On the next page click on the Settings tab to adjust the settings.

5. Click on the 'config vars' button.

6. Supply a KEY of PORT and it's value of 8000. Then click on the "add" button.

7. Buildpacks now need to be added.

8. These install future dependancies that we need outside of the requirements file.

9. Select Python first and then node.js and click save.

10. Make sure they are in this order.

11. Then go to the deploy section and choose your deployment method.

12. To connect with github select github and confirm.

13. Search for your repository select it and click connect.

14. You can choose to either deploy using automatic deploys which means heroku will rebuild the app everytime you push your changes.

15. For this option choose the branch to deploy and click enable automatic deploys.

16. This can be changed at a later date to manual.

17. Manual deployment deploys the current state of a branch.

18. Click deploy branch.

19. We can now click on the open App button above to view our application.
***

## Credits 

I watched and read so much material when making this project. Most people have different approach some more interesting than others, I tried to do it my own way. This is the material I researched to help make my project possible. Mentor Gareth Mcgirr who helped with the project from the concept and troubleshooting he made the project a lot less stressful. 

https://github.com/gsamarakoon/Fun-projects-for-Python/blob/master/A%20game%20of%20BlackJack.ipynb

https://www.youtube.com/watch?v=8QTsK1aVMI0

https://samarakoon-gayan.medium.com/a-game-of-black-jack-on-python-as-a-fun-exercise-3cd54efb9d83

https://www.youtube.com/watch?v=aryte85bt_M

https://replit.com/@BeauCarnes/blackjack-python

https://www.youtube.com/watch?v=l2n65N0C-ls

https://github.com/wynand1004/Projects/blob/master/Cards/deck_of_cards.py

https://www.askpython.com/python/examples/terminal-hi-lo-game-in-python

https://www.codespeedy.com/blackjack-console-game-using-python/
***