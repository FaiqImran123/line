from os import remove
from shape import *
from time import sleep

class Line(Shape):
    def __init__(self, screen, x1, y1, x2, y2, color='BLUE', background_color ="WHITE"):
        super().__init__(screen, color)
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

    def draw(self):
        py.draw.line(self.screen, self.color, (self.__x1, self.__y1), (self.__x2, self.__y2))
        py.display.update()
    def remove(self):
        py.draw.line(self.screen, self.bg, (self.__x1, self.__y1), (self.__x2, self.__y2))
        py.display.update()
    def move(self, x, y):
        self.remove()
        self.__x1 +=x
        self.__x2 +=x
        self.__y1 +=y
        self.__y2 +=y
        self.draw()
    def change_size(self, val):
        self.remove()
        py.draw.line(self.screen, self.color, (self.__x1, self.__y1), (self.__x2+val, self.__y2+val))
        py.display.update()
        
                
