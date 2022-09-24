class Player:
    points = 300
    guess = ''
    addiction = 1
    def playAgain(self, decision):
        if(decision == 'y'):
            self.addiction = 1
            print()
            return self.addiction
        else:
            self.addiction = 0
            print(f"Congrats you dont have a gambling addiction. 😉 Your end score was {self.points}!")
            return self.addiction
    
    def loser(self, score):
        if(score <= 0):
            print(f"HAHAHAHA Sucker! You lost all of your points! You have {self.points} points! See Ya!")
            self.addiction = 0
            return self.addiction
        else:
            self.addiction = 1
            return self.addiction