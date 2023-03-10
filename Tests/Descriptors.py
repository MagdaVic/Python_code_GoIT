class Integer:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError('Координати мають бути цілими')
    def __set_name__(self, owner, name):
        self.name = '_'+name

    def __get__(self, instance, owner):
        return getattr(instance,self.name)
        # return instance.__dict__[self.name]


    def __set__(self, instance, value):
        self.verify_coord(value)
        print(f"__set__{self.name}:{value}, self:{self}, instance:{instance}")
        setattr(instance,self.name,value)
        # instance.__dict__[self.name]=value

class Point3D:
    x=Integer()
    y=Integer()
    z=Integer()
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p=Point3D(1,2,4)
print(p.__dict__)
p.x=6
print(p.x)
