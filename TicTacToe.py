#Tic Tac Toe Assignment
#By: Garren Meisman

lineOne = []
lineTwo = []
lineThree = []
inbetweenLine=[]
def main():
    person = 1
    grid()

def grid():
    lineOne = ["1", "|", "2", "|", "3"]
    lineTwo = ["4", "|", "5", "|", "6"]
    lineThree = ["7", "|", "8", "|", "9"]
    inbetweenLine = ["-", "+", "-", "+", "-"]
    print(*lineOne)
    print(*inbetweenLine)
    print(*lineTwo)
    print(*inbetweenLine)
    print(*lineThree)
    return lineOne and lineTwo and lineThree and inbetweenLine

def move(number, person):
    if (0 < number < 4):
        line = lineOne
    elif (3 < number < 7):
        line = lineTwo
    elif (6 < number < 10):
        line = lineThree
    else:
        print("This is not a number option")

    place = line.index(number)

    if (person == 1):
        if(line[place] != "X" or line[place] != "O"):
            line = line.replace(number, "X")
            person = 0
            return line
        else:
            print("That spot has already been taken")
    else:
        if(line[place] != "X" or line[place] != "O"):
            line = line.replace(number, "O")
            person = 1
            return line
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