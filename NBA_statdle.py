import pandas as pd
import random
import re
import sys
import seaborn as sns
import matplotlib.pyplot as plt
from argparse import ArgumentParser

class Game:
    """ Base class for NBA statdle game
    
    Attributes:
        name(str,optional):name of the player.
        path(str): path to the basketball players information file
        df(Pandas Dataframe): dataframe of the NBA players with stats
        filtered_df(Pandas Dataframe): dataframe of the NBA players with stats but filtered
    """
    def __init__(self, path, name = None): #Abdulrezak
        """This will initailize the class with a file name of a csv file.

        Args:
            path (string): name of the csv file with NBA players
            name (string, optional): Name of the user who is playing the game. Defaults to None.
        """
        self.df = pd.read_csv(path, encoding = "ISO-8859-1")
        name = input(f"Input your name: ")
        self.name = name
        
        self.clean_data()
        
    def clean_data(self): #Jesse
        """ Filter the dataframe only contain columns "FULL_NAME", "TEAM",
            "POS", "MPG", and "PPG" if self.df is not None. Else it prints out "This program is not running"
            
        Args:
        filtered_df(Pandas Dataframe): the dataframe of NBA players with filtered stats
        """
        self.filtered_df = self.df[["FULL_NAME", "TEAM", "POS", "MPG", "PPG"]] if self.df is not None else print("This program is not running")
        
    def choose_player(self): #Jake
        """Selects random player that the user will guess for

        Returns:
            player(Pandas Dataframe): Dataframe of the Player that users will guess
        """
        player = self.filtered_df.iloc[random.randint(0, 715)]
        
        return player
        
    def play(self): #Wonwoo
        """This is where playing the guessing game will happen. It will prompt the user to input his/her name, input a player.
        Then it will let the user know if the player is not in the database or if the user is correct or what stats they got
        correct and wrong. When the user gets the guess correct, it will calculate the score then print out the result. If the user
        has beaten the best record, it will congratulate the user, or else it will just write the score in the scores file.
        Also, when the score becomes 0, it will quit the game because the user is out of guesses. If the user
        guess was not correct, it will compare the stats of the user guessed player and the chosen player and print out what was
        wrong and what was correct.
        
        Wonwoo was mainly in charge of this method. Skills of f-string was shown. 
        Jake also contributed towards writing this method to show the skill of merging dataframes. 
        
        Args:
        chosen_player(Pandas Dataframe): Dataframe of the Player that users will guess
        score(int): Starting score will be 100 and will be deducted 10 points each round.
        round(int): Starting round. It will increase when the player guesses for the wrong player.
        
        """        
        chosen_player = self.choose_player()
        score = 100
        round = 1
        
        print("Name of the player: ",self.name)
        
        while True:    
            print("score: ", score - (round - 1) * 10)
            print("round: ", round)
            
            self.read_in_score("Highest_Score.txt")
            
            user_guess = input(f"Make a guess: ")
            
            player_list = self.filtered_df["FULL_NAME"].str.lower().values.tolist()
            
            newlist = [x.lower() for x in player_list if user_guess.lower() in x]
            
            if len(newlist) == 0:
                print(f"Your guess is not in our database!")
                continue
            
            user_guesss = self.filtered_df[self.filtered_df["FULL_NAME"] == user_guess].index.values
            chosen_player_stats = self.filtered_df[self.filtered_df["FULL_NAME"] == chosen_player["FULL_NAME"]].index.values
            
            guess_df = self.filtered_df.iloc[user_guesss]
            answer_df = self.filtered_df.iloc[chosen_player_stats]
            
            merged_df = guess_df.merge(answer_df, how="outer")
                
            if user_guess.lower() == chosen_player["FULL_NAME"].lower():
                print("You are correct") 
                result = score.__sub__(10 * (round - 1))
                print(f"Your score is: {result}")
                
                if result == 0:
                    print(f"You are out of guesses!")
                    break
                
                with open("scores.txt", "a", encoding="utf-8") as f:
                    f.write(str(result) + "\n")
                best_score = self.find_score("Highest_Score.txt")
                if int(best_score) < result:
                    print(f"Conglatulations! You have beaten the record!")
                    self.high_score("Highest_Score.txt", result)
                break
            
            else:
                if merged_df["TEAM"][0] == merged_df["TEAM"][1]:
                    print("You got the team correct!")
                else:
                    print("You got the team wrong!")

                if merged_df["POS"][0] in merged_df["POS"][1]:
                    print("You got the position correct!") 
                else:
                    print("You got the position wrong!")

                if merged_df["MPG"][0] > merged_df["MPG"][1]:
                    print("Your guess has higher MPG!")
                elif merged_df["MPG"][0] < merged_df["MPG"][1]:
                    print("Your guess has lower MPG!")
                else:
                    print("You got the MPG correct!")

                if merged_df["PPG"][0] > merged_df["PPG"][1]:
                    print("Your guess has higher PPG!")
                elif merged_df["PPG"][0] < merged_df["PPG"][1]:
                    print("Your guess has lower PPG!")
                else:
                    print("You got the PPG correct!")
                round += 1
                
    def high_score(self, path, score): # Wonwoo
        """This method will read in a file and take the score of the game to record.

        Args:
            path (string): file to record the best score
            score (int): score of the game that user scored.
            
        Side Effects:
            it will create a file if there is none and record the best score.
        """
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"Your best score is: {score}")
            
    def read_in_score(self, path): # TJ
        """this method reads in the file that contains the recorded scores

        Args:
            path (string): name of the file
        """
        with open(path, "r", encoding="utf-8") as f:
            line = f.readlines()
            print(line)
            
    def find_score(self, path): # TJ
        """This method looks for the best score in the a file with regex.

        Args:
            path (string): name of the file

        Raises:
            ValueError: If there is no match it will raise a value error

        Returns:
            best_score(int): It returns the match which is the best score
        """
        with open(path, "r", encoding="utf-8") as f:
            line = f.readlines()
            match = re.search(r"(?P<score>\d+)", str(line))
            if match == None:
                raise ValueError("You don't have any scores")

            best_score = match.group(1)
            
            return best_score

    def plot(self, path): # Abdulrezak
        """Visualizes the scores of each games. It will show if the player has made progress or not. It also enables the users to compare between games.

        Args:
            path (str): the path to the score file. 
        """
        with open(path) as f:
            score = f.readlines()
       
        score = [int(x.strip()) for x in score]
        score.sort()
        
        plt.plot(score, color='green', marker='o',mfc='green')
        plt.ylabel('Score') 
        plt.xlabel('Rounds') 
        plt.title("Score Board") 
        plt.show()
    
    def __sub__(self, other): #Wonwoo
        """magic method that will calculate the score

        Args:
            other (int): it will take in a number which will be (round - 1) * 10.
            This will able us to calculate the score number of rounds taken for the user to guess correct number * 10.

        Returns:
            int: it will return the subtraction from the score(100) - (round - 1) * 10.
        """
        return self - other
            
def main(file): #Jake
    """Runs the game and plots player score(s)

    Args:
        file (.csv): NBA players with their respective statistics
    """
    game = Game(file)
    game.play()
    game.plot("scores.txt")
    
def parse_args(arglist): #Jesse
    """ Parse command-line argument.
    
    Expect one mandatory argument:
        - str: a path to a csv file that contains all player data.
    
    Args:
        arglist (list of str): command-line arguments.
    
    Returns:
        namespace: an object with one attribute, the file path.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="path to NBA player list csv file")
    args = parser.parse_args(arglist)
    return args

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)

"""
To run this program, enter in "python3 NBA_statdle.py NBA_stats.csv"
Have fun :)
"""