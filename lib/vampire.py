class Vampire:
    def __init__(self, name, pet = "bat", thirsty = True):
        self.name = name
        self.pet = pet
        self.thirsty = thirsty

    def is_thirsty(self):
        return self.thirsty

    def drink(self):
        self.thirsty = False
