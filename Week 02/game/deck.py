import random
class Deck:
    ogValue = random.randint(1, 13)
    newValue = random.randint(1, 13)
    def changeValue(self):
        self.ogValue = self.newValue
        return self.newValue