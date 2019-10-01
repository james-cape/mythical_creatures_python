class Centaur:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.standing = True
        self.cranky_level = 0

    def shoot(self):
        self.cranky_level += 1
        if self.is_cranky() == False and self.is_laying() == False:
            return "Twang!!!"
        else:
            return "NO!"

    def run(self):
        self.cranky_level += 1
        if self.is_cranky() == False and self.is_laying() == False:
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

    def sleep(self):
        if self.standing == True:
            return "NO!"
        else:
            self.cranky_level = 0

    def lay_down(self):
        self.standing = False

    def is_laying(self):
        return not self.standing

    def stand_up(self):
        self.standing = True

    def drink_potion(self):
        if self.is_standing() == True and self.is_cranky() == False:
            return "Now I'm sick"
        elif self.is_standing() == True:
            self.cranky_level = 0
        else:
            return "Can't, I'm laying"
