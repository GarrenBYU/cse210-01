from game.casting.actor import Actor


class Artifact(Actor):    

    def __init__(self):
        self._message = ""

    def set_message(self, message):
        self._message = message
    def get_message(self):
        return self._message
