class Pirate:
    def __init__(self, name, job = "Scallywag", curse_level = 0):
        self.name = name
        self.job = job
        self.curse_level = curse_level

    def is_cursed(self):
        if self.curse_level == 0:
            return False
