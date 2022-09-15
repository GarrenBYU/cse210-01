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

main()