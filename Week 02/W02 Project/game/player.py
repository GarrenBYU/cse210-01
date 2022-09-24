class Player:

    """The player is here for their records and choices.

    The Player is the one making choices and has the points and records tied to their class

    Attributes:
    points (int): This is the count of points that the player has
    guess (str): This is the value of the guess of the player. It is either higher or lower
    addiction (boolean): This is a true or false boolean if it should continue looping or not
    """    
    points = 300
    guess = ''
    addiction = True
    def playAgain(self, decision):

        """Begins the game

        Args:
            self (Player): an instance of Player.
            decision (str): It is the decision of the player to continue playing or not
        """
        if(decision == 'y'):
            self.addiction = True
            print()
            return self.addiction
        else:
            self.addiction = False
            print(f"Congrats you dont have a gambling addiction. 😉 Your end score was {self.points}!")
            return self.addiction
    
    def loser(self, score):
    
        """Begins the game

        Args:
            self (Player): an instance of Player.
            score (int): This is the number of points that the player has
        """
        if(score <= 0):
            print(f"HAHAHAHA Sucker! You lost all of your points! You have {self.points} points! See Ya!")
            self.addiction = False
            return self.addiction
        else:
            self.addiction = True
            return self.addiction