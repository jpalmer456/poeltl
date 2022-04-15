from argparse import ArgumentParser
import sys
import random
import pandas as pd

class Player:
   """Parent class that will be inherited to subclass of HumanPlayer and ComputerPlayer
  
    Attributes:
        name (str): name of the player
    """

   def __init__(self, name):
    """initializes a player with a name
    """
    def __init__(self, name):
        """initializes a player with a name

        Args:
            name (str): name of the player
    """
      
   def turn(self, game):
        """Take a turn
 
        Args:
            game (Poeltl): snapshot of the current game
	Returns:
		str: the player’s guess
        """
class HumanPlayer(Player):
    """subclass of Player class that inherits __init__() method but overrides turn() method. It will take players move as input and return it
	Attributes:
        name (str): name of the player
    """
   def turn(self, game):
        """a method that will keep track of turns
 
        Args:
            game (Poeltl): represents the current state of the game
	Returns:
	    str: the player’s guess
        """
    
class ComputerPlayer(Player):
    """is a subclass of Player that overrides both __init__() and turn() methods. This class will make a computer player guess players.
   
Attributes:
       name(str): name of the computer
       player(list): list of strings from excel/txt file that computer can draw to guess competing against the player
    """
 
    def __init__(self, name, player_list):
        """this method will store name and player list.
 
        Args:
           name(str): name of the computer
           player_list(list): list of strings from panda that computer can draw to guess when taking turns
        """
 
    def turn(self, game):
       """this method will guess a player with randomly at first and then with using the hints, it will eventually guess the player
 
        Args:
            game (Poeltl): represents the current game
      
        Returns:
           guess (str): the word that computer is guessing
        """
 
  
    
class Poeltl:
    """Class used to create the framework of the Poeltl game where we the user has to guess an NBA player's name until they get the right player.
 
    Args:
        file (panda): dataframe for opening the file
    """


    def __init__(self, file):
        """Opens and reads the file using panda   

    Args:
        file (panda): dataframe for opening the file

        """

 
          
    def getPlayer(self):
        """ Chooses a player a random   
    Attributes:
        name(str): name of the computer
        player(list): list of strings from excel/txt file that computer can draw to guess competing against the player
        """
 
    def check_answer(self, player_guess, answer):
        """ Checks if the guess of the NBA player is right or wrong.
    Args:
	    player_guess (str): the guess the user makes
	    answer (str): the correct answer of the player
    Returns:
	    Returns whether the guess was right or wrong.
        """
    
<<<<<<< HEAD
    def reveal_hint(self, player_guess, stats, answer):
        """ Reveals a hint to the user if they get the answer wrong.
        Args:
        	player_guess (str): the guess the user makes
        	stats (float/str):
	    	Answer (str): the stat revealed about the player we’ll show the user
        Returns:
	        Returns the stat (hint) about the player.
        """
  
    def guessed_answers(self):
        """ Checks if the guess of the NBA player is right or wrong.
        Args:
	        player_guess (str) = the guess the user makes
	        answer (str) = the correct answer of the player
        Returns:
	        Returns whether the guess was right or wrong.
        """
  
    def play(self):
        """ play the game
	    
        Side effects:
        """
    def turn(self, player):
        """ manage players’s turn.
        Args:
	        Player(player): the player turn,
        Side effect : 
            Modify —---- functions 
        """
    def outcome(self):
        """Determine if the game is over.
	    Returns: 
            “Win” or “lose” if all the players have lost, or None if the game is not over”””
 
 
        """
 
def main(player_list, human_player, computer_player = False, compyter_player_list = None):
    """Set up and play a game of hangman.
 
   Args:
       player_list (str): lists of players and stats
       human_players (list of str): names of the human players, if any.
       computer_player (bool, optional): if True, a computer player will be
           created. Defaults to False.
       computer_player_list (list of str, optional): a list of players that the
           computer player "knows". If None, player_list will be used. Defaults
           to None.
    """

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.player_list, args.names, args.computer_player, args.computer_player_list)
=======
>>>>>>> 2693c6a79398cc48f21aa7c3c661bdf5ba091df6
>>>>>>> 2d631bd3c1118f7eedaec78cbaea0d967073ce62
