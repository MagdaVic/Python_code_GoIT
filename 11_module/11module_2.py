class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, new_x):
        if isinstance(new_x, int):
            self.__x=new_x
        else:
            raise TypeError ('Enter int number x')

    @y.setter
    def y(self, new_y):
        if isinstance(new_y, int):
            self.__y=new_y
        else:
            raise TypeError ('Enter int number y')

point = Point(-1, 10)

print(point.x)  # 5
print(point.y)  # 10
point.x=5.8
print(point.x)
    