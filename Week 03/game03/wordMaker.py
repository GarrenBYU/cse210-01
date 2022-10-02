import random
class Word_Maker:
    """The Word Maker that provides most of the Word Maker information

    The Word Maker is the class that provides the new random word that is going to be used.

    Attributes:
    words(array): This is an array of strings that has random words that can be chosen
    newWord (int): This is a random value that is going to pick the word
    """
    words = ['help', 'destroy', 'begin', 'transform', 'stop', 'amazing', 'bananas', 'incredible', 'again', 'loser', 'winner']
    wordslen = len(words)

    def randomWord(self):
        newNumber = random.randint(1, self.wordslen)
        newWord = self.words[newNumber]
        return newWord