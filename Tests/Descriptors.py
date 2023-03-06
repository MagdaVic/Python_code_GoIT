class Point3D:
    def __init__(self, x):
        self._x = x
        # self._y=y
        # self_z=z

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError('Координати мають бути цілими')

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, coord):
        self.verify_coord(coord)
        self._x = coord


p = Point3D(5)
print(p.x)
p.x = 8
print(p.x)
