class Unicorn:
    def __init__(self, name, color="white"):
        self.name = name
        self.color = color

    def is_white(self):
        return self.color == "white"

    def say(self, words):
        return f"**;* {words} **;*"
