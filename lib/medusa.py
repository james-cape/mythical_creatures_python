class Medusa:
    def __init__(self, name, statues = []):
        self.name = name
        self.statues = statues

    def stare(self, victim):
        self.statues.append(victim)

class Person:
    def __init__(self, name):
        self.name = name
