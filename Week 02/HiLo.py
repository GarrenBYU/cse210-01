from asyncio.windows_events import NULL
import random
class Player:
    player_number = 1
    points = 300
    guess = ''
    guessint = NULL
    def guessNumber(self):
        guessint = int(self.guess)
        return guessint


class Card:
    def newValue(self):
        self.value = random.randint(1, 14)
        return self.value

def main():
    addiction = 1
    while(addiction == 1):
        card = Card
        card.value = (random.randint(1, 13))
        OGcard = card.value
        print(f"The card is: {card.value} ")
        next_card = Card
        next_card.value = (random.randint(1, 13))
        Player.guess = input("Higher or Lower? [h/l] ")
        hiLo(OGcard, next_card.value)
        print(f"Next card was: {next_card.value}")
        score = Player.points
        print(f"Your score is: {score}")
        again = input("Play again? [y/n] ")
        addiction = playAgain(again)

def hiLo(current, next):
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

def playAgain(decision):
    if(decision == 'y'):
        addiction = 1
        print()
        return addiction
    else:
        addiction = 2
        print(f"Congrats you dont have a gambling addiction. 😉 Your end score was {Player.points}!")
        return addiction

if __name__ == "__main__":
    main()