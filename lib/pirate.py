class Pirate:
    def __init__(self, name, job = "Scallywag", curse_level = 0, booty = 0):
        self.name = name
        self.job = job
        self.curse_level = curse_level
        self.booty = booty

    def is_cursed(self):
        if self.curse_level < 3:
            return False
        else:
            return True

    def commit_heinous_act(self):
        self.curse_level += 1

    def rob_ship(self):
        self.booty += 100
