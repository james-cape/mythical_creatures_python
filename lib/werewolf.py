class Werewolf:
    def __init__(self, name, location = "nowhere", human_state = True, hungry = False):
        self.name = name
        self.location = location
        self.human_state = human_state
        self.hungry = hungry

    def is_human(self):
        return self.human_state

    def change(self):
        if self.human_state == True:
            self.hungry = True
            self.human_state = False
        else:
            self.human_state = True

    def is_wolf(self):
        return not self.human_state

    def is_hungry(self):
        return self.hungry

    def consume(self, consumed):
        if self.human_state == True:
            return "No one was consumed"
        else:
            consumed.status = "Dead"
            self.hungry = False

class Victim:
    def __init__(self):
        self.status = "Alive"
