# Statdle
#### Purpose of each file
1. NBA_statdle.py - contains the Python code written to make the program run. In other words, it is the backbone of our project. 
2. NBA_stat.csv - CSV file that contains all the player's names along with their stats. This csv will be used to create a dataframe and compare with the user's input to check whether or not the guess is correct.
3. scores.txt - This .txt file is used to store the user's score from the game. The scores will then be combined/added. The scores will also be used to plot our graph.
4. Highest_Score.txt - Obtains score from the output of the Python program and compares it to the score that existed in Highest_Score.txt. If the new score is higher, we replace the highest score.

#### How to run the program
If using Windows, within the command line, type "python NBA_statdle.py NBA_stat.csv".
If using Mac, within the command line, type "python3 NBA_statdle.py NBA_stat.csv".

#### How to interpret the output
Our program is very similar to Poeltl and Wordle, where the system generates a random player for the user to guess. The user will then have to guess the correct player until their score (hp point) reaches zero. Whenever the player inputs an incorrect guess, the program will then compare the guess with the already generated NBA player. If the guess is wrong, then the user will get hints (e.g.: "PPG is higher", "Wrong team"). If the player guessed correctly, it will display the score along with a score chart and end the program.


