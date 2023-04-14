# -*- coding: utf-8 -*-
################################################
# Bridge
# ----------------------------------------------
# Connecting components together through abstractions.
# A bridge is a mechanism that decouples an interface (hierarchy)
# from an implementation (hierarchy).
# ----------------------------------------------
# Motivation:
# Bridge prevents a Cartesian product complexity explosion
# Example:
# - Base class ThreadScheduler.
# - Can be preemptive or cooperative
# - Can run on Windows or Unix.
# - End up with a 2X2 scenario: WindowsPTS, UnixPTS, WindowsCTS, UnixCTS.
# 
# Instead of doing this:
#                                                       >> WindowsCTS
#                       >> CooperativeThreadScheduler [ 
#                                                       >> UnixCTS
# >> ThreadScheduler [
#                                                       >> WindowsPTS
#                       >> PreemptiveThreadScheduler  [
#                                                       >> UnixPTS
# Do this:
# 
# PreemptiveThreadScheduler                                                                   >> WindowsScheduler
#                             ] ThreadScheduler (platformScheduler) --> IPlatformScheduler [
# CooperativeThreadScheduler                                                                  >> LinuxScheduler
# 
# Bridge pattern avoids the entity explosion.
# ----------------------------------------------
# Summary:
# - Decouple abstraction from implementation.
# - Both can exist as hierarchies.
# - A stronger form of encapsulation.
################################################

# Objects: circle, square
# Draws implementation: vector, raster
# Combination result: circleVector, circleRaster, squareVector, squareRaster
from abc import ABC


class Renderer(ABC):
  def render_circle(self, radius): pass
  def render_square(self, side): pass
  

class VectorRenderer(Renderer):
  def render_circle(self, radius):
    print(f'Drawing a circle of radius {radius}')
  
  def render_square(self, side):
    print(f'Drawing a square of side {side}')


class RasterRenderer(Renderer):
  def render_circle(self, radius):
    print(f'Drawing pixels for a circle of radius {radius}')

  def render_square(self, side):
    print(f'Drawing pixels for a square of side {side}')


class Shape:
  def __init__(self, renderer):
    self.renderer = renderer
    
  def draw(self): pass
  def resize(self, factor): pass


class Circle(Shape):
  def __init__(self, renderer, radius):
    super().__init__(renderer)
    self.radius = radius

  def draw(self):
    self.renderer.render_circle(self.radius)
    
  def resize(self, factor):
    self.radius *= factor
  
  
if __name__ == '__main__':
  print('Bridge')
  print('................................................')
  raster = RasterRenderer()
  vector = VectorRenderer()
  
  circle1 = Circle(vector, 5)
  circle1.draw()
  circle1.resize(2)
  circle1.draw()
  
  circle2 = Circle(raster, 5)
  circle2.draw()
  circle2.resize(2)
  circle2.draw()
  