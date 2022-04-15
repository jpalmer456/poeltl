import random
 
class Player:
    """Parent class that will be inhereted to subclass of HumanPlayer and ComputerPlayer
    
    Attributes:
        name (str): name of the player
    """
    def __init__(self, name):
        """initializes a player with a name

<<<<<<< HEAD
class Poeltl:
    def __init__(self, game):
        self.game = game
        
    def check_answer(input, answer):
        
        return input == answer
=======
        Args:
            name (str): name of the player
        """
        
    def turn(self, game):
        """_summary_

        Args:
            game (_type_): _description_
        """
class HumanPlayer(Player):
    """subclass of Player class that inherits __init__() method
    """
    def turn(self, game):
        """a method that will keep track of turns

        Args:
            game (_type_): _description_
        """
      
class ComputerPlayer(Player):
  
    def __init__(self):
  
    def turn(self, game):
      
class Poeltl:
    def __init__(self, file):
       self.f = open(file, 'r')
      
    def getPlayer():
       #chooses random players
    def reveal_hint():
       #reveals hint
    def check_answer():
       #check whether the answer is correct
    def guessed_answers():
   #     #gathers guessed names and deletes them out of the unguessed player names
    def play():
       #plays the game
    def turn():
       #take turn guessing players
    def outcome():
       #result of who wins

def read_file(path):
    #reads in the file and put players in a dictionary as a key and their stats as the value

def main():
    
>>>>>>> 2693c6a79398cc48f21aa7c3c661bdf5ba091df6
