#Tic Tac Toe Assignment
#By: Garren Meisman

win=""
lineOne = ["1", "|", "2", "|", "3"]
lineTwo = ["4", "|", "5", "|", "6"]
lineThree = ["7", "|", "8", "|", "9"]
inbetweenLine = ["-", "+", "-", "+", "-"]
def main():
    player = 1
    #grid
    while (win != "victory"):
        print(*lineOne)
        print(*inbetweenLine)
        print(*lineTwo)
        print(*inbetweenLine)
        print(*lineThree)
        desicionOne = input("What number do you want to place? ")
        move(desicionOne, 1, lineOne, lineTwo, lineThree)
        desicionTwo = input("What number do you want to place? ")
        move(desicionTwo, 2, lineOne, lineTwo, lineThree)
    if (win == "victory"):
        print(f"Player {player} wins")

def move(number, player, line1, line2, line3):
    if (0 < int(number) < 4):
        line = line1
        return line
    elif (3 < int(number) < 7):
        line = line2
        return line
    elif (6 < int(number) < 10):
        line = line3
        return line
    else:
        print("This is not a number option")

    place = line.index(number)

    if (player == 1):
        if(line[place] != "X" or line[place] != "O"):
            line = line.remove(number)
            print(line)
            line = line.insert(place, "X")
            player = 2
            return line and player
        else:
            print("That spot has already been taken")
    else:
        if(line[place] != "X" or line[place] != "O"):
            line = line.remove(number)
            line = line.insert(place, "O")
            player = 1
            return line and player
        else:
            print("That spot has already been taken")

def victory(line, place):
    count = 1
    prev = count - 1
    cont = count + 1
    win = ""
    if (line[count] == line[prev] == line[cont]):
        win = "victory"
        return win
    elif (lineOne[place] == lineTwo[place] == lineThree[place]):
        win = "victory"
        return win    
    elif (lineOne[0] == lineTwo[1] == lineThree[2]):
        win = "victory"
        return win
    elif (lineOne[2] == lineTwo[1] == lineThree[0]):
        win = "victory"
        return win

main()