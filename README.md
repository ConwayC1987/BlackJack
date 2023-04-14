 **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

# BLACKJACK
This is terminal based game of the classic casino card game, Blackjack, using Python. The game allows a player to play against a computer dealer and follow the standard rules of Blackjack.


## Pre-planning
A workflow model was needed for the project and I decided to us Lucid chart to help plan the project out.

## Structure of the code
### Class used
Deck
Card
Player


## Game Flow


## Features left to implement


## Technologies used


## Testing

| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |


## Bugs
There is a bug in the code that for some reason 10 are being displayed on the terminal as 1 instead of 10. 
- At the start I thought it was aces that were showing as 1 but eventualy it was discovered it was the 10 that was causing the problem. I think the reason for the error is 10 was an extra digit to the rest of cards and when I split the ranks and suits to draw a card using assci art it is being split at 1 and 0 rather than being split at 10 and then the suit. This took over 7 days to discover what card it was happening with and as to why it might be happening.

## Deployment
Navigate to heroku.com & log in.

Click "new" and create a new App.

Give the application a name and then choose your region and Click "Create app".

On the next page click on the Settings tab to adjust the settings.

Click on the 'config vars' button.

Supply a KEY of PORT and it's value of 8000. Then click on the "add" button.

Buildpacks now need to be added.

These install future dependancies that we need outside of the requirements file.

Select Python first and then node.js and click save.

Make sure they are in this order.

Then go to the deploy section and choose your deployment method.

To connect with github select github and confirm.

Search for your repository select it and click connect.

You can choose to either deploy using automatic deploys which means heroku will rebuild the app everytime you push your changes.

For this option choose the branch to deploy and click enable automatic deploys.

This can be changed at a later date to manual.

Manual deployment deploys the current state of a branch.

Click deploy branch.

We can now click on the open App button above to view our application.

## Credits 

https://github.com/gsamarakoon/Fun-projects-for-Python/blob/master/A%20game%20of%20BlackJack.ipynb

https://www.youtube.com/watch?v=8QTsK1aVMI0

https://samarakoon-gayan.medium.com/a-game-of-black-jack-on-python-as-a-fun-exercise-3cd54efb9d83

https://www.youtube.com/watch?v=aryte85bt_M

https://replit.com/@BeauCarnes/blackjack-python

https://www.youtube.com/watch?v=l2n65N0C-ls

https://github.com/wynand1004/Projects/blob/master/Cards/deck_of_cards.py

https://www.askpython.com/python/examples/terminal-hi-lo-game-in-python

https://www.codespeedy.com/blackjack-console-game-using-python/