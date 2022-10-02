class Sky_Diver:
    """The sky diver is here for their records and choices.

    The sky diver is the one making choices and has the points and records tied to their class

    Attributes:
    lives (int): This is the count of possible times the sky diver can guess the wrong letter
    guess (str): This is the value of the guess of the sky diver. It is either higher or lower
    crazy (boolean): This is a true or false boolean if it should continue looping or not
    """    
    lives = 5
    guess = ''
    crazy = True
    def playAgain(self, decision):

        """Begins the game

        Args:
            self (Player): an instance of skydiver.
            decision (str): It is the decision of the sky diver to continue playing or not
        """
        if(decision == 'y'):
            self.crazy = True
            print()
            return self.crazy
        else:
            self.crazy = False
            print(f"Congrats you aren't crazy and don't want to risk another life. 👌")
            return self.crazy
    
    def loser(self):
    
        """Begins the game

        Args:
            self (Player): an instance of sky diver.
            score (int): This is the number of points that the sky diver has
        """
        if(self.lives <= 0):
            print(f"Well you screwed up! You are now falling to the inevitable. Send a good word for me! ☠️")
            self.crazy = False
            return self.crazy
        else:
            self.crazy = True
            return self.crazy