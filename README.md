README.md

This game is called "A Day in the Life of a Holy Cross Student" and players are going to simulate living a day as a Holy Cross student. The goal is to finish the day with a positive number of points. If the user score is above zero by the end of the day, at 8 PM, the user wins; if the score is zero or below, user loses.

The game plays out in a fixed sequence of events, and at each step there might be randomness and the user is asked a yes/no question or prompted to pick from a list of options. The user has to type their answer and press Enter

At 3 AM, the alarm rings. Choose whether to get up right away or hit snooze.
1. Snoozing costs −5 points each time, and the alarm keeps ringing every hour until 7 AM (or until you finally get up). User will study python before 7 AM. After 7 AM, breakfast at Kimball earns +5 points.
2. Waking up immediately earns you +10 points. User will drink tea and check the weather. The weather is randomly chosen from sunny, windy, rainy, foggy, or stormy. User gets to decide whether or not they wish to surf before school starts. Surfing is only safe in sunny, windy, or rainy weather and +15 points; in foggy or stormy weather user cannot surf, so user studies Python instead +10 points. If user chooses to surf, he will go to Newport beach and at 7 AM he will choose between morning mass or ice cream. Attending morning mass +10 points. Getting Clemie's ice cream −5 points.

At 8 AM, a random number of classes (1–8) is generated. When drowsiness hits, user will choose to sleep in class with -10 points and a chalk to the head or to fight it off +10 points.
At 5 PM, user will choose to meet friends at Crossroads for dinner or eat alone.+10 points for meeting friends. 
At 8 PM it is Bedtime. The final score is tallied and win or lose is announced.

The player's state is represented with the varriable points, that starts at 0 and is calculated and accumulated in every activity function. 







