class Dragon:
    def __init__(self, name, color, rider, hungry = True, eaten = 0):
        self.name = name
        self.color = color
        self.rider = rider
        self.hungry = hungry
        self.eaten = eaten

    def is_hungry(self):
        if self.eaten > 2:
            self.hungry = False
        return self.hungry

    def eat(self):
        self.eaten += 1
