class Ogre:
    def __init__(self, name, home = "Swamp"):
        self.name = name
        self.home = home
        self.swings = 0

    def encounter(self, human):
        human.encounter_counter += 1
        if human.notices_ogre() == True:
            self.swing_at(human)

    def swing_at(self, human):
        self.swings += 1
        if self.swings % 2 == 0:
            human.knocked_out = True

    def apologize(self, human):
        human.knocked_out = False

class Human:
    def __init__(self, name = "Jane"):
        self.name = name
        self.encounter_counter = 0
        self.knocked_out = False

    def notices_ogre(self):
        return self.encounter_counter % 3 == 0
