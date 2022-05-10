import pandas as pd
import random
import re
import sys
import seaborn as sns
import matplotlib.pyplot as plt
from argparse import ArgumentParser

class Game:
    def __init__(self, path, name = None): #Abdul
        self.df = pd.read_csv(path, encoding = "ISO-8859-1")
        name = input(f"Input your name: ")
        self.name = name
        
        self.clean_data()
        
    def clean_data(self): #Jesse
        self.filtered_df = self.df[["FULL_NAME", "TEAM", "POS", "MPG", "PPG"]] if self.df is not None else print("This program is not running")
        
    def choose_player(self): #Jake
        player = self.filtered_df.iloc[random.randint(0, 715)]
        
        return player
        
    def play(self): #Abdul Jesse Jake Wonwoo TJ        
        cp = self.choose_player()
        score = 100
        round = 1
        
        print("Name of the player: ",self.name)
        
        while True:    
            print("score: ", score - (round - 1) * 10)
            print("round: ", round)
            print(cp)
            
            self.read_in_score("Highest_Score.txt")
            
            ug = input(f"Make a guess: ")
            
            player_list = self.filtered_df["FULL_NAME"].str.lower().values.tolist()
            
            newlist = [x.lower() for x in player_list if ug.lower() in x]
            
            if len(newlist) == 0:
                print(f"Your guess is not in our database!")
                continue
            
            ugs = self.filtered_df[self.filtered_df["FULL_NAME"] == ug].index.values
            cps = self.filtered_df[self.filtered_df["FULL_NAME"] == cp["FULL_NAME"]].index.values
            
            guess_df = self.filtered_df.iloc[ugs]
            answer_df = self.filtered_df.iloc[cps]
            
            a = guess_df.merge(answer_df, how="outer")
                
            if ug.lower() == cp["FULL_NAME"].lower():
                print("You are correct") 
                result = score.__sub__(10 * (round - 1))
                print(f"Your score is: {result}")
                
                if result == 0:
                    print(f"You are out of guesses!")
                    break
                
                with open("scores.txt", "a", encoding="utf-8") as f:
                    f.write(str(result) + "\n")
                bs = self.find_score("Highest_Score.txt")
                if int(bs) < score:
                    print(f"Conglatulations! You have beaten the record!")
                    self.high_score("Highest_Score.txt", score)
                break
            
            else:
                if a["TEAM"][0] == a["TEAM"][1]:
                    print("You got the team correct!")
                else:
                    print("You got the team wrong!")

                if a["POS"][0] in a["POS"][1]:
                    print("You got the position correct!") 
                else:
                    print("You got the position wrong!")

                if a["MPG"][0] > a["MPG"][1]:
                    print("Your guess has higher MPG!")
                elif a["MPG"][0] < a["MPG"][1]:
                    print("Your guess has lower MPG!")
                else:
                    print("You got the MPG correct!")

                if a["PPG"][0] > a["PPG"][1]:
                    print("Your guess has higher PPG!")
                elif a["PPG"][0] < a["PPG"][1]:
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

    def plot(self, path): # Abdul
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
    game = Game(file, "Brian")
    game.play()
    game.plot("scores.txt")
    
def parse_args(arglist): #Jesse
    parser = ArgumentParser()
    parser.add_argument("file", help="path to NBA player list csv file")
    args = parser.parse_args(arglist)
    return args

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)

