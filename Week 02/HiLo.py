import random
class Player:
    points = 300
    guess = ''
    def playAgain(self, decision):
        if(decision == 'y'):
            Dealer.addiction = 1
            print()
            return Dealer.addiction
        else:
            Dealer.addiction = 0
            print(f"Congrats you dont have a gambling addiction. 😉 Your end score was {self.points}!")
            return Dealer.addiction


class Deck:
    ogValue = random.randint(1, 14)
    newValue = random.randint(1, 14)
    def changeValue(self):
        self.ogValue = self.newValue
        return self.newValue

class Dealer:
    previous_card = Deck.ogValue
    current_card = Deck.newValue
    addiction = 1
    def choice(self, current, next):
        if(Player.guess == "l"):
            if(current > next):
                Player.points = Player.points + 100
                return Player.points
            else:
                Player.points = Player.points - 75
                return Player.points
        elif(Player.guess == "h"):
            if(current < next):
                Player.points = Player.points + 100
                return Player.points
            else:
                Player.points = Player.points - 75
                return Player.points

    def loser(self, score):
        if(score <= 0):
            print(f"HAHAHAHA Sucker! You lost all of your points! You have {Player.points} points! See Ya!")
            self.addiction = 0
            return self.addiction
        else:
            self.addiction = 1
            return self.addiction


def main():
    while(Dealer.addiction == 1):
        print(f"The card is: {Dealer.previous_card} ")
        user_choice = input("Higher or Lower? [h/l] ")
        Player.guess = user_choice
        Dealer.choice(Dealer, Dealer.previous_card, Dealer.current_card)
        print(f"Next card was: {Dealer.current_card}")
        score = Player.points
        print(f"Your score is: {score}")
        Dealer.addiction = Dealer.loser(Dealer, score)
        if(Dealer.addiction == 1):
            again = input("Play again? [y/n] ")
            Dealer.addiction = Player.playAgain(Player, again)
            Dealer.previous_card = Dealer.current_card
            Deck.newValue = random.randint(1, 14)
            Dealer.current_card = Deck.newValue

if __name__ == "__main__":
    main()