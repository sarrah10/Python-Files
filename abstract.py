from abc import ABC, abstractmethod


class shape(ABC):  #abstract class coz abstract method is defined
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def draw(self):
        pass        #cannot define in this

class triangle(shape):
    def __init__(self, name):
        super().__init__(name)
    def draw(self):
        print("drawing triangle")

#if draw() is not called so objects will not be created of that class
class circle(shape):
    def __init__(self, name):
        super().__init__(name)
    def hello(self):
        print("Hello world")
    def draw(self):  
        print("drawing circle")

t = triangle("Triangle")
t.draw()
c=circle("circle")
c.hello()
c.draw()