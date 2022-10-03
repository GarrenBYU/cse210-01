from game03.wordMaker import Word_Maker
from game03.skyDiver import Sky_Diver
class Ref():
    
    """The person that leads the game and takes from the parachute

    The Ref leads the game as well as keeps up on if the player lost or not

    Attributes:
    word (str): The current word trying to be guessed
    user_choice (str): Gets the user's choice whether the next card will be higher or lower
    """
    word = ''
    def start_game(self):
        """Begins the game

        Args:
            self (ref): an instance of ref.
        """
        wordMaker = Word_Maker
        skyDiver = Sky_Diver
        #while(skyDiver.crazy == True):
        i = 1
        win = False
        while(win == False):
            self.parachute()
            if(i==1):
                newWord = wordMaker.randomWord(Word_Maker)
                spaces = self.spaces(newWord)
                i = i + 1
            print(' ' .join(spaces))
            user_choice = input("What letter do you want to guess? ")
            user_choice = user_choice.lower()
            counter = 0
            stop = False
            for i in newWord:
                if user_choice == i and stop == False:
                    print(f"Congrats you guessed a letter!")
                    self.replaceSpaces(user_choice, newWord, spaces)
                    counter = counter + 1
                    stop = True
                else:
                    counter = counter + 1
                if(counter == len(newWord) and stop == False):
                    skyDiver.lives = skyDiver.lives - 1
                    print(f"That is not a letter! You have {skyDiver.lives} lives left.")
            again = skyDiver.loser(Sky_Diver)
            if(again == False):
                #playAgain = input("Play again? [y/n] ")
                #skyDiver.crazy = skyDiver.playAgain(skyDiver, playAgain)
                win = True
                return win
            win = True
            for i in spaces:
                if i == '_':
                    win = False
            if win == True:
                print("Congrats You Won! 🥇")
                skyDiver.crazy = False
                win = True
    def parachute(self):
        skyDiver = Sky_Diver
        counter = 5
        place = 0
        dontFall = [' ___', '/   \ ', ' ___', '\   /', ' \ /']
        while(counter > 0):
            if counter <= skyDiver.lives:
                while(counter != 0):
                    print(dontFall[place])
                    counter = counter - 1
                    place = 1 + place
            else:
                counter = counter - 1
                dontFall.pop(0)
        print('  O')
        print(' /|\ ')
        print(' / \ ')

    def spaces(self, word):
        spaces = ["_"]
        while(len(spaces) < len(word)):
            spaces.append('_')
        return spaces

    def replaceSpaces(self, letter, word, spaces):
        bo = 0
        for i in word:
            if i == letter:
                spaces[bo] = letter
                bo = bo + 1
            else:
                bo = bo + 1
        return spaces
            
        