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
    
>>>>>>> 2d631bd3c1118f7eedaec78cbaea0d967073ce62
