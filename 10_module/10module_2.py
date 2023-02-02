class Animal:
    nickname = None
    weight = None

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight


animal = Animal('dggg', 34)
print(animal.nickname)
