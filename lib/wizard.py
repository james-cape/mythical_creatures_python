class Wizard:
    def __init__(self, name, bearded = True):
        self.name = name
        self.bearded = bearded

    def is_bearded(self):
        return self.bearded

    def incantation(self, phrase):
        return f"sudo {phrase}"
