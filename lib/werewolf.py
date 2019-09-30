class Werewolf:
    def __init__(self, name, location = "nowhere", human_state = True):
        self.name = name
        self.location = location
        self.human_state = human_state

    def is_human(self):
        return self.human_state


    def change(self):
        if self.human_state == True:
            self.human_state = False
        else:
            self.human_state = True

    def is_wolf(self):
        return not self.human_state
