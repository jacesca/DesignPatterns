# -*- coding: utf-8 -*-
################################################
# FACTORY METHOD
# ----------------------------------------------
# Factory Method is a creational design pattern that 
# provides an interface for creating objects in a 
# superclass, but allows subclasses to alter the 
# type of objects that will be created.
# ----------------------------------------------
# A factory method is a static method that creates objects.
# A factory is any entity that can take care of object creation.
# A factory can be external or reside inside the object as an inner class.
# Hierarchies of factories can be used to create related objects.
# ----------------------------------------------
# Motivation: Object creation logic becomes too
# convoluted.
# Initializer is not descriptive.
# - Name is always __init__.
# - Can not overload with same sets of arguments
#   with different names.
# - Can turn into 'optional parameter hell'.
# Wholesale (extensive) object creation, (non-piecewise,
# unlike Builder) can be outsourced to:
# - A separate method (Factory Method).
# - That may exidt in a separate class (Factory).
# - Can create hierarchy of factories with Abstract Factory.
# ----------------------------------------------
# What is a Factory?
# A component responsible solely for the wholesale (not
# piecewise) creation of objects.
# ----------------------------------------------
# FACTORY
# It is the implementation of the SRP or SOC principle.
# In most cases, a factory is just a separate class, 
# which is full of factory methods, not necessarily
# static ones that allows you to create objects.
################################################


# # ----------------------------------------------
# # First Approach
# # ----------------------------------------------
# class Point:
#   def __init__(self, x, y):
#     """
#     What happen if you want to initialize the point in a Polar system?
#     """
#     self.x = x
#     self.y = y
#
#   def __str__(self):
#     return f'Point(x={self.x}, y={self.y})'
#
#
# if __name__ == '__main__':
#   p = Point(2, 3)
#   print(p)  
    
  
  
# # ----------------------------------------------
# # Second Approach
# # Make the builder (__init__) take control on the system type to create the object.
# # ----------------------------------------------
# from enum import Enum
# from math import sin, cos
#
#
# class CoordinateSystem(Enum):
#   CARTESIAN = 1
#   POLAR = 2
#
#
# class Point:
#   def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
#     """
#     Second approach
#     The constructor breaks the OCP.
#     """
#     self.system = system
#     if system == CoordinateSystem.CARTESIAN:
#       self.x = a
#       self.y = b
#     elif system == CoordinateSystem.POLAR:
#       self.x = a * cos(b)
#       self.y = a * sin(b)
#
#   def __str__(self):
#     return f'Point(x={self.x}, y={self.y})'
#
#
# if __name__ == '__main__':
#   p = Point(2, 3)
#   print(p)  
#
#   pp = Point(10, 120, CoordinateSystem.POLAR)
#   print(pp)
  
  
# # ----------------------------------------------
# # Third Approach
# # Create separated builder for each system with their own variables.
# # ----------------------------------------------
# from enum import Enum
# from math import sin, cos
#
#
# class CoordinateSystem(Enum):
#   CARTESIAN = 1
#   POLAR = 2
#
#
# class Point:  
#   def __init__(self, x, y):
#     """
#     Factory approach
#     """
#     self.x = x
#     self.y = y
# 
#   def __str__(self):
#     return f'Point(x={self.x}, y={self.y})'
# 
#   @staticmethod
#   def new_cartesian_point(x, y):
#     """
#     If you get too many factory methods inside a class, 
#     it might make sense to actually move them out of the class 
#     or at least to try and group them in a separate entity.
#     """
#     return Point(x, y)
# 
#   @staticmethod
#   def new_polar_point(rho, theta):
#     return Point(rho * cos(theta), rho * sin(theta))
# 
#
# if __name__ == '__main__':
#   p = Point(2, 3)
#   print(p)  
#
#   pc = Point.new_cartesian_point(5, 10)
#   print(pc)
#
#   pp = Point.new_polar_point(10, 120)
#   print(pp)


# # ----------------------------------------------
# # Fourth Approach
# #     If you get too many factory methods inside a class, 
# #     it might make sense to actually move them out of the class 
# #     or at least to try and group them in a separate entity.
# # ----------------------------------------------
# from enum import Enum
# from math import sin, cos
#
#
# class CoordinateSystem(Enum):
#   CARTESIAN = 1
#   POLAR = 2
#
#
# class Point:
#   def __init__(self, x, y):
#     """
#     Factory approach
#     """
#     self.x = x
#     self.y = y
#
#   def __str__(self):
#     return f'Point(x={self.x}, y={self.y})'
#
# class PointFactory:
#   @staticmethod
#   def new_cartesian_point(x, y):
#     """
#     If the point class changes, then all of these methods need to be
#     updated in consequence.
#     """
#     return Point(x, y)
#
#   @staticmethod
#   def new_polar_point(rho, theta):
#     return Point(rho * cos(theta), rho * sin(theta))
#
#
# if __name__ == '__main__':
#   p = Point(2, 3)
#   print(p)  
#
#   pc = PointFactory.new_cartesian_point(5, 10)
#   print(pc)
#
#   pp = PointFactory.new_polar_point(10, 120)
#   print(pp)


# # ----------------------------------------------
# # Fourth Approach
# #     Minimizing the dependency of PointFactory on Point class.
# # ----------------------------------------------
# from enum import Enum
# from math import sin, cos
#
#
# class CoordinateSystem(Enum):
#   CARTESIAN = 1
#   POLAR = 2
#
#
# class Point:
#   def __init__(self, x=0, y=0):
#     """
#     Factory approach
#     """
#     self.x = x
#     self.y = y
#
#   def __str__(self):
#     return f'Point(x={self.x}, y={self.y})'
#
# class PointFactory:
#   @staticmethod
#   def new_cartesian_point(x, y):
#     """
#     If the point class changes, then all of these methods need to be
#     updated in consequence.
#     """
#     p = Point(x, y)
#     p.x = x
#     p.y = y
#     return p
#
#   @staticmethod
#   def new_polar_point(rho, theta):
#     p = Point()
#     p.x = rho * cos(theta)
#     p.y = rho * sin(theta)
#     return p
#
# if __name__ == '__main__':
#   p = Point(2, 3)
#   print(p)  
#
#   pc = PointFactory.new_cartesian_point(5, 10)
#   print(pc)
#
#   pp = PointFactory.new_polar_point(10, 120)
#   print(pp)


# ----------------------------------------------
# Fifth Approach
#     Move the Factory class inside the Object class.
# ----------------------------------------------
from enum import Enum
from math import sin, cos


class CoordinateSystem(Enum):
  CARTESIAN = 1
  POLAR = 2


class Point:
  def __init__(self, x=0, y=0):
    """
    Factory approach
    """
    self.x = x
    self.y = y
  
  def __str__(self):
    return f'Point(x={self.x}, y={self.y})'
  
  class PointFactory:
    def new_cartesian_point(self, x, y):
      """
      If the point class changes, then all of these methods need to be
      updated in consequence.
      """
      p = Point(x, y)
      p.x = x
      p.y = y
      return p
    
    @staticmethod
    def new_polar_point(rho, theta):
      p = Point()
      p.x = rho * cos(theta)
      p.y = rho * sin(theta)
      return p
  
  factory = PointFactory()
  
if __name__ == '__main__':
  p = Point(2, 3)
  print(p)  
  
  pc = Point.PointFactory().new_cartesian_point(5, 10)
  print(pc)
  
  pp = Point.factory.new_polar_point(10, 120)
  print(pp)
