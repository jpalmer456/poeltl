# Statdle

Documentation (please name your file README.md or README.pdf), including
An explanation of the purpose of each file in your repository
Clear instructions on how to run your program from the command line
Clear instructions on how to use your program and/or interpret the output of the program, as applicable
Attribution: in order to evaluate whether each member has made a substantial, original contribution to the project, please clearly and unambiguously indicate who is the primary author of each major function/method. You do not need to attribute minor program components, such as an if __name__ == "__main__": statement.
An annotated bibliography of all sources you used to develop your project. For each source, explain how you used the source.

#### Purpose of each file
1. NBA_statdle.py - contains the python code written to make the program run. In other words, the backbone of our project. 
2. NBA_stat.csv - CSV file that contains all the players name along with their stats. This csv will be used to create a dataframe and compare with the user's input to check wether or not the guess is correct.
3. scores.txt - This txt file is used to store the users score from the game. The scores will then be combined/added. The scores will also be used to plot our graph.
4. Highest_Score.txt - Obtains score from the output of the python program and compare it to the score that existed in Highest_Score.txt. If the new score is higher, we replace the highest score.

#### How to run the program
If using windows, within the command line, type "python NBA_statdle.py NBA_stat.csv".
If using mac, within the command line, type "python3 NBA_statdle.py NBA_stat.csv".

#### How to interpret the output
Our program is very similar to poeltl and wordle, where the system generates a random player for the user to guess. The user will then have to guess the correct player until their score (hp point) reaches zero. Whenever the player input an incorrect guess, the program will then compare the guess with the already generated NBA player. If the guess is wrong, then the user will get hints (e.g: "PPG is higher", "Wrong team"). If the player guessed correctly, it will display the score along with a score chart and ends the program.

#### Attribution
Abdul was responsible for the init() method and plot() method. There, he met requirements of optional parameters and visualizing data with seaborn. Jesse was responsible for the clean_data() method and parse_args() function. In these methods and functions Jesse used conditional expression and parse_args functions to meet the two requirements that he needed. Wonwoo was in charge of the play() method, sub() method and high score() method. In the play() method Wonwoo met f-string, in sub() method he used magic methods other than init(). TJ was responsible for read_in_score and find_score methods. In the read_in_score method TJ met the requirement with using the with statements and in the find_score method, he used the regex to meet the requirements. Jake was in charge of choose_players and main and helped Wonwoo with the play() method. In the choose_player() method and play() method, he used concatenating, merging to perform operations on Pandas DataFrame and a list comprehension.

#### Annotated Bibliography 
1. https://www.nbastuffer.com/2021-2022-nba-player-stats/
We obtained our CSV file from this site. Which is then used to create our dataframe. The web is constantly being updated, so some informtion might not match with the file we used.
2. https://poeltl.dunk.town/
We obtained our inspiration from poeltl. This game was used to help layout the flowchart of our program.
