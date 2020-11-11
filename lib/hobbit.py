class Hobbit:
    def __init__(self, name, disposition = "homebody", age = 0, height = "short"):
        self.name = name
        self.disposition = disposition
        self.age = age
        self.height = height

    def celebrate_birthday(self):
        self.age += 1

    def is_adult(self):
        return self.age > 32

    def is_old(self):
        return self.age >= 101

    def has_ring(self):
        return self.name == "Frodo"

    def is_short(self):
        return self.height
