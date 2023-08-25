import math
class Shape():
    def area(self):
        pass

class Square(Shape):
    def area(self,side_length):
        return side_length**2


class Traingle(Shape):
    def area(self,base,height):
        return 0.5*base*height


class Circle(Shape):
    def area(self,radius):
        return math.pi*(radius**2)


sq=Square()
print(sq.area(5))

Tr=Traingle()
print(Tr.area(2,4))

Cr=Circle()
print(Cr.area(5))


