import random
class Player:
    player_number = 1
    points = 300
    guess = ''

class Card:
    value = random.randrange(1, 14)
def main():
    card = Card
    next_card = Card
    print(f"The card is: {card.value} ")
    Player.guess = input("Higher or Lower? [h/l] ")

def hiLo(current, next):
    if(Player.guess = "l"):
        if(current < next):
            Player.points = Player.points + 100
        else:
            Player.points = Player.points - 75
            

if __name__ == "__main__":
    main()