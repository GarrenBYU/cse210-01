#Tic Tac Toe Assignment
#By: Garren Meisman
def main():
    lineOne = []
    lineTwo = []
    lineThree = []
    inbetweenLine=[]
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

main()