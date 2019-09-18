class Hobbit:
    def __init__(self, name, disposition = "homebody", age = 0):
        self.name = name
        self.disposition = disposition
        self.age = age

    def celebrate_birthday(self):
        self.age += 1

    def is_adult(self):
        False if self.age <= 32 else True
