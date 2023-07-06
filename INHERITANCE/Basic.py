import math

class shape:
    def __init__(self,border,bodercolor) :
        self.border=border
        self.bodercolor=bodercolor

    def add(self,color):
        self.bodercolor=color

    def __str__(self) -> str:
        return f"{self.__class__.__name__},{self.border},{self.bodercolor}"

class circle(shape):
    def __init__(self, border,bordercolor,borderthick,radius,borderradius):
        super().__init__( border,bordercolor)
        self.radius=radius
        self.borderthick=borderthick
        self.borderradius=borderradius

    def __str__(self) -> str:
         return f"{self.__class__.__name__}, border: {self.border}, bodercolor: {self.bodercolor}, radius: {self.radius}, borderradius: {self.borderradius}"
    
    def area(self,radius):
        return math.pi *radius**2





circle1=circle(3,3,3,3,3)
print(circle1)

circle1.add("green")
print(circle1)

print(circle1.area(1))