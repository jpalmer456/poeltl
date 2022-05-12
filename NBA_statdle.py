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
    """
    def __init__(self, path, name = None): #Abdulrezak
        self.df = pd.read_csv(path, encoding = "ISO-8859-1")
        name = input(f"Input your name: ")
        self.name = name
        
        self.clean_data()
        
    def clean_data(self): #Jesse
        """ Filter the dataframe only contain columns "FULL_NAME", "TEAM",
            "POS", "MPG", and "PPG".
        """
        self.filtered_df = self.df[["FULL_NAME", "TEAM", "POS", "MPG", "PPG"]] if self.df is not None else print("This program is not running")
        
    def choose_player(self): #Jake
        """Selects random player that the user will guess for

        Returns:
            string: Player that users will guess
        """
        player = self.filtered_df.iloc[random.randint(0, 715)]
        
        return player
        
    def play(self): #Abdulrezak Jesse Jake Wonwoo TJ        
        chosen_player = self.choose_player()
        score = 100
        round = 1
        
        print("Name of the player: ",self.name)
        
        while True:    
            print("score: ", score - (round - 1) * 10)
            print("round: ", round)
            print(chosen_player)
            
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
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"Your best score is: {score}")
            
    def read_in_score(self, path): # TJ
        with open(path, "r", encoding="utf-8") as f:
            line = f.readlines()
            print(line)
            
    def find_score(self, path): # TJ
        with open(path, "r", encoding="utf-8") as f:
            line = f.readlines()
            match = re.search(r"(?P<score>\d+)", str(line))
            if match == None:
                raise ValueError("You don't have any scores")

            best_score = match.group(1)
            
            return best_score

    def plot(self, path): # Abdulrezak
        """Visuals of the player score

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
        return self - other
            
def main(file): #Jake
    """Runs the game and plots player score(s)

    Args:
        file (.csv): NBA players with their respective statistics
    """
    game = Game(file, "Brian")
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

