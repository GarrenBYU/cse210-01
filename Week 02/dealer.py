import random
from player import Player
from deck import Deck
class Dealer:
    previous_card = Deck.ogValue
    current_card = Deck.newValue
    def start_game(self):
        player = Player()
        deck = Deck()
        while(player.addiction == 1):
            print(f"The card is: {self.previous_card} ")
            user_choice = input("Higher or Lower? [h/l] ")
            player.guess = user_choice
            self.choice(self.previous_card, self.current_card, player)
            print(f"Next card was: {self.current_card}")
            score = player.points
            print(f"Your score is: {score}")
            player.addiction = player.loser(score)
            if(player.addiction == 1):
                again = input("Play again? [y/n] ")
                player.addiction = player.playAgain(again)
                self.previous_card = self.current_card
                deck.newValue = random.randint(1, 14)
                self.current_card = deck.newValue
    def choice(self, current, next, player):
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