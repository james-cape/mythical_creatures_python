class Wizard:
    def __init__(self, name, bearded = True, rest_level = 0):
        self.name = name
        self.bearded = bearded
        self.rest_level = rest_level

    def is_bearded(self):
        return self.bearded

    def incantation(self, phrase):
        return f"sudo {phrase}"

    def is_rested(self):
        return self.rest_level < 3

    def cast(self):
        self.rest_level += 1
        return "MAGIC MISSILE!"
