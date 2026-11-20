README.md

This game is called "A Day in the Life of a Holy Cross Student" and players are going to simulate living a day as a Holy Cross student. The goal is to finish the day with a positive number of points. If the user score is above zero by the end of the day, at 8 PM, the user wins; if the score is zero or below, user loses. If the score is exactly 0, the user looses by almost winning the game.

The game plays out in a fixed sequence of events, and at each step there might be randomness and chioces and the user is asked a yes/no question or prompted to pick from a list of options to proceed on. The user has to type their answer and all answers are validated.

The player's state is represented with the varriable called points, and it is passed into and out of every function in order to track the user state. The points starts at 0 every morning and is constantly updated in every activity function. The last function of the main code evaluates the points and tells the user whether they have won or lost the game.

According to the peer reviews, the program was improved in the following 8 ways:
1. attribute error for the time module is fixed
2. docstrings are added
3. validation of all inputs are added, and put the validation functions into a new python file and imported it to main
4. created more than 6 functions and incorporated more randomness
5. made the activity of both going to mass and having icecream as available options simultaneously
6. changed the structure and orientation of the code to make it more readble and straightforward
7. worked to exceed expectations of the rubric, as it was the goal peer reviewers set which seems doable
8. modified readme and the spelling errors throughout the files







