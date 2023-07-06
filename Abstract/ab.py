import math
from abc import ABC, abstractmethod



class shape:
   
    def __init__(self,border,bodercolor,borderthick,borderradius) :
        self.border=border
        self.bodercolor=bodercolor
        self.borderthick=borderthick
        self.borderradius=borderradius 

    def add(self,color):
        self.bodercolor=color


    @abstractmethod
    def area(self):
        pass
        
        
    # def __str__(self) -> str:
    #     return f"{self.__class__.__name__},{self.border},{self.bodercolor}"

class circle(shape):
    def __init__(self, border,bordercolor,borderthick,radius,borderradius):
        super().__init__( border,bordercolor,borderthick,borderradius)
        self.radius=radius
        
        
    def area(self):
        return math.pi *self.radius**2
    

class rectangle(shape):
    def __init__(self, border,bordercolor,height,radius,width,borderthick,borderradius):
        super().__init__( border,bordercolor,borderthick,borderradius)
        self.radius=radius
        self.height=height
        self.width=width
        

    def area(self):
        return self.width *self.height
    
    # def __str__(self) -> str:
    #      return f"{self.__class__.__name__}, border: {self.border}, bodercolor: {self.bodercolor}, radius: {self.radius}, borderradius: {self.borderradius}"
  





circle1=circle(3,3,3,3,3)
print(circle1.area())

rec1=rectangle(3,3,3,3,3,3,3)
print(rec1.area())


