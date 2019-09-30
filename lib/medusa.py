class Medusa:
    def __init__(self, name, statues = []):
        self.name = name
        self.statues = statues

    def stare(self, victim):
        if len(self.statues) == 3:
            self.statues[0].stoned_status = False
            self.statues.pop(0)
            victim.stoned_status = True
            self.statues.append(victim)
        else:
            victim.stoned_status = True
            self.statues.append(victim)

class Person:
    def __init__(self, name, stoned_status = False):
        self.name = name
        self.stoned_status = stoned_status

    def is_stoned(self):
        return self.stoned_status
