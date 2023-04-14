# -*- coding: utf-8 -*-
################################################
# Bridge Coding Exercise
# ----------------------------------------------
# You are given an example of an inheritance hierarchy which results in 
# Cartesian-product duplication.
# Please refactor this hierarchy, giving the base class Shape  a constructor 
# that takes an interface Renderer  defined as
#   class Renderer(ABC):
#       @property
#       def what_to_render_as(self):
#           return None
# as well as VectorRenderer  and RasterRenderer  classes. 
# Each inheritor of the Shape  abstract class should have a constructor that takes a 
# Renderer  such that, subsequently, each constructed object's __str__()  operates 
# correctly, for example,
# str(Triangle(RasterRenderer()) # returns "Drawing Triangle as pixels" 
################################################
# class Shape:
#     def __init__(self):
#         self.name = None
#
#
# class Triangle(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Triangle'
#
#
# class Square(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Square'
#
#
# class VectorSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as lines'
#
#
# class RasterSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as pixels'

# # imagine VectorTriangle and RasterTriangle are here too

from unittest import TestCase, main
from abc import ABC


class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None
        
        
# TO DO: reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer
class RasterRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return ' as pixels'
        

class VectorRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return ' as lines'        
        

class Shape:
    def __init__(self, render):
        self.render = render
        # self.name = None
        
    def __str__(self):
        return 'Drawing ' + type(self).__name__ + self.render.what_to_render_as
        # return 'Drawing ' + self.name + self.render.what_to_render_as


class Triangle(Shape):
     def __init__(self, render):
         super().__init__(render)
         # self.name = 'Triangle'


class Square(Shape):
     def __init__(self, render):
         super().__init__(render)
         # self.name = 'Square'




class Evaluate(TestCase):
    def test_square_vector(self):
        sq = Square(VectorRenderer())
        self.assertEqual(str(sq), 'Drawing Square as lines')

    def test_pixel_triangle(self):
        tr = Triangle(RasterRenderer())
        self.assertEqual(str(tr), 'Drawing Triangle as pixels')



if __name__ == '__main__':
    main() 