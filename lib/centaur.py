class Centaur:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.standing = True
        self.cranky_level = 0

    def shoot(self):
        self.cranky_level += 1
        if self.is_cranky() == False:
            return "Twang!!!"
        else:
            return "NO!"

    def run(self):
        self.cranky_level += 1
        if self.is_cranky() == False:
            return "Clop clop clop clop!!!"
        else:
            return "NO!"

    def is_cranky(self):
        if self.cranky_level < 3:
            return False
        else:
            return True

    def is_standing(self):
        return self.standing
