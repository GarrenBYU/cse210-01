#Tic Tac Toe Assignment
#By: Garren Meisman
win=""
OGGridOne = ["1", "|", "2", "|", "3"]
OGGridTwo = ["4", "|", "5", "|", "6"]
OGGridThree = ["7", "|", "8", "|", "9"]
OGlineOne = ["1", "|", "2", "|", "3"]
OGlineTwo = ["4", "|", "5", "|", "6"]
OGlineThree = ["7", "|", "8", "|", "9"]
inbetweenLine = ["-", "+", "-", "+", "-"]
usedNumbers = []
def main():
    player = 1
    i = 0
    win=0
    desicionTwo = '10'
    n= 0
    #grid
    lineOne = OGlineOne
    lineTwo = OGlineTwo
    lineThree = OGlineThree
    print(*lineOne)
    print(*inbetweenLine)
    print(*lineTwo)
    print(*inbetweenLine)
    print(*lineThree)
    while(win == 0):
        while(n == 0 or 0 >= int(desicionOne) > 9 or w == True):
            desicionOne = input("What number do you want to place Player 1? ")
            n=1
            w = usedNumber(desicionOne, lineOne, lineTwo, lineThree, OGGridOne, OGGridTwo, OGGridThree)
        n=0
        w=True
        move(desicionOne, 1, lineOne, lineTwo, lineThree)
        print(*lineOne)
        print(*inbetweenLine)
        print(*lineTwo)
        print(*inbetweenLine)
        print(*lineThree)
        if(victory(desicionOne, lineOne, lineTwo, lineThree, win) == 1):
            break
        i = i+1
        if(i >= 9):
            break
        while(n == 0 or 0 >= int(desicionTwo) > 9 or w == True):
            desicionTwo = input("What number do you want to place Player 2? ")
            n=1
            w = usedNumber(desicionTwo, lineOne, lineTwo, lineThree, OGGridOne, OGGridTwo, OGGridThree)
        n = 0
        w=True
        move(desicionTwo, 2, lineOne, lineTwo, lineThree)
        if(victory(desicionOne, lineOne, lineTwo, lineThree, win) == 1):
            break
        print(*lineOne)
        print(*inbetweenLine)
        print(*lineTwo)
        print(*inbetweenLine)
        print(*lineThree)
        i = i+1

    if (victory(desicionOne, lineOne, lineTwo, lineThree, win) == 1):
        print(f"Player {player} wins")
    else:
        print("Good game it is a Cats Game!")

def move(number, player, line1, line2, line3):
    if (0 < int(number) < 4):
        line = line1
    elif (3 < int(number) < 7):
        line = line2
    elif (6 < int(number) < 10):
        line = line3
    else:
        print("This is not a number option")

    place = line.index(number)

    if (player == 1):
        if(line[place] != "X" or line[place] != "O"):
            line.remove(number)
            line.insert(place, "X")
            player = 2
            return line and player
        else:
            print("That spot has already been taken")
    else:
        if(line[place] != "X" or line[place] != "O"):
            line.remove(number)
            line.insert(place, "O")
            player = 1
            return line and player
        else:
            print("That spot has already been taken")

def victory(number, line1, line2, line3, score):
    if (0 < int(number) < 4):
        line = line1
        OGline = OGGridOne
    elif (3 < int(number) < 7):
        line = line2
        OGline = OGGridTwo
    elif (6 < int(number) < 10):
        line = line3
        OGline = OGGridThree
    else:
        print("This is not a number option")

    place = OGline.index(number)
    count = 2
    prev = count - 2
    cont = count + 2
    if (line[count] == line[prev] == line[cont]):
        score = 1
        return score
    elif (line1[place] == line2[place] == line3[place]):
        score = 1
        return score    
    elif (line1[0] == line2[2] == line3[4]):
        score = 1
        return score
    elif (line1[4] == line2[2] == line3[0]):
        score = 1
        return score

def usedNumber(number, line1, line2, line3, OG1, OG2, OG3):
    if (0 < int(number) < 4 ):
        place = OG1.index(number)
        if(OG1[place] == line1[place]):
            return False
        else:
            print("That spot was already taken")
            return True
    elif (3 < int(number) < 7):
        place = OG2.index(number)
        if(OG2[place] == line2[place]):
            return False
        else:
            print("That spot was already taken")
            return True
    elif (6 < int(number) < 10):
        place = OG3.index(number)
        if(OG3[place] == line3[place]):
            return False
        else:
            print("That spot was already taken")
            return True
    else:
        print("This number or place is not an option")
        return True

if __name__ == "__main__":
    main()