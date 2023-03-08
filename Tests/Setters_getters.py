class Point3D:
    def __init__(self, x):
        print('Працює ініціалізація')
        self.x = x
        self._x = x
        # print(self._x)
        print('Ініціалізація завершилась')


        # self._y=y
        # self_z=z

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError('Координати мають бути цілими')

    @property
    def x(self):
        print('Працює геттер')
        print(f'Геттер: {self._x }')
        return self._x

    @x.setter
    def x(self, coord):
        # self.verify_coord(coord)
        print('Працює сеттер')
        self._x = coord
        print(f'Сеттер: {self._x }')


p = Point3D(5.5)
# print(dir(p))
p.x

print(p.__dict__)


# p.x = 8
# print(p.x)
# print(p.__dict__)
