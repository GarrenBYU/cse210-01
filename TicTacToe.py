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

def move(line, place, number, person):
    if (person == 1):
        if(line[place] != "X" or line[place] != "O"):
            line = line.replace(number, "X")
            return line
        else:
            print("That spot has already been taken")
    else:
        if(line[place] != "X" or line[place] != "O"):
            line = line.replace(number, "O")
            return line
        else:
            print("That spot has already been taken")

main()