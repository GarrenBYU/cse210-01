import random
from game.player import Player
from game.deck import Deck
class Dealer:

    """The person that leads the game and deals from the Deck

    The Dealer leads the game as well as keeps up on if the player lost or not

    Attributes:
    previous_card (int): This is the orginal card at the beginning and then it is the previous card
    current_card (int): This is the new card drawn
    user_choice (str): Gets the user's choice whether the next card will be higher or lower
    """

    previous_card = Deck.ogValue
    current_card = Deck.newValue
    def start_game(self):
        """Begins the game

        Args:
            self (Dealer): an instance of Dealer.
        """
        player = Player()
        deck = Deck()
        while(player.addiction == True):
            print(f"The card is: {self.previous_card} ")
            user_choice = input("Higher or Lower? [h/l] ")
            player.guess = user_choice
            self.choice(self.previous_card, self.current_card, player)
            print(f"Next card was: {self.current_card}")
            score = player.points
            print(f"Your score is: {score}")
            player.addiction = player.loser(score)
            if(player.addiction == True):
                again = input("Play again? [y/n] ")
                player.addiction = player.playAgain(again)
                self.previous_card = self.current_card
                deck.newValue = random.randint(1, 13)
                self.current_card = deck.newValue
    def choice(self, current, next, player):
        """Determines point value for the choice

        Args:
            self (Dealer): an instance of Dealer.
            current (): Is the first or original card.
            next (): Is the new card to compare the original to.
            player (Player): Is the player class.
        """
        if(player.guess == "l"):
            if(current > next):
                player.points = player.points + 100
                return player.points
            else:
                player.points = player.points - 75
                return player.points
        elif(player.guess == "h"):
            if(current < next):
                player.points = player.points + 100
                return player.points
            else:
                player.points = player.points - 75
                return player.points