class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def change_color(self, color):
        Animal.color = color


first_animal = Animal('ds', 34)
second_animal = Animal('sdd', 45)
first_animal.change_color('red')
second_animal.change_color('red')

print(first_animal.color, second_animal.color, Animal.color)
