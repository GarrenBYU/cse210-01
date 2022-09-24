import random
class Deck:
    ogValue = random.randint(1, 14)
    newValue = random.randint(1, 14)
    def changeValue(self):
        self.ogValue = self.newValue
        return self.newValue