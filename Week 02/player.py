from dealer import Dealer
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