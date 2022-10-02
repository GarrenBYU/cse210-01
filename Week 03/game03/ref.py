from pyparsing import Word
from game03.wordMaker import Word_Maker
from skyDiver import Sky_Diver
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
        while(skyDiver.crazy == True):
            while(1 == 1):
                i = 1
                self.parachute()
                if(i==1):
                    word = wordMaker.randomWord
                    spaces = self.spaces()
                    i = i + 1
                user_choice = input("What letter do you want to guess? ")
                user_choice = user_choice.lower
                for i in word:
                    if user_choice == word[i]:
                        print(f"Congrats you guessed a letter!")
                        self.replaceSpaces(user_choice, word, spaces)
                    else:
                        skyDiver.lives = skyDiver.lives - 1
                        print(f"That is not a letter! You have {skyDiver.lives} lives left.")
                skyDiver.loser()
                if(skyDiver.crazy == True):
                    again = input("Play again? [y/n] ")
                    skyDiver.crazy = skyDiver.playAgain(again)
    def parachute(self):
        skyDiver = Sky_Diver
        dontFall = ['___', '/   \ ', '___', '\   /', '\  /']
        for i in dontFall:
            if i >= skyDiver.lives:
                print(dontFall[i])

    def spaces(self, word):
        spaces = []
        while(len(spaces) < len(word)):
            spaces.append('_ ')
        return spaces

    def replaceSpaces(self, letter, word, spaces):
        bo = 0
        while(bo != -1):
            index = word.findIndex(letter)
            spaces[index] = letter
        return spaces
            
        