import random
class Deck:

    """The Deck that provides most of the Deck information

    The Deck is the cards that are used in the rest of the game

    Attributes:
    ogValue(int): This is a random value that is assigned to the first card
    newValue (int): This is a random value that is assigned to the second card
    """
    ogValue = random.randint(1, 13)
    newValue = random.randint(1, 13)
    def changeValue(self):

        """Makes a new value for the cards

        Args:
            self (deck): an instance of deck.
        """
        self.ogValue = self.newValue
        return self.newValue