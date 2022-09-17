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
def main():
    player = 1
    i = 0
    win=0
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
        desicionOne = input("What number do you want to place Player 1? ")
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
        desicionTwo = input("What number do you want to place Player 2? ")
        move(desicionTwo, 2, lineOne, lineTwo, lineThree)
        print(i)
        if(victory(desicionOne, lineOne, lineTwo, lineThree, win) == 1):
            break
        print(*lineOne)
        print(*inbetweenLine)
        print(*lineTwo)
        print(*inbetweenLine)
        print(*lineThree)
        i = i+1
        print(i)
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

if __name__ == "__main__":
    main()