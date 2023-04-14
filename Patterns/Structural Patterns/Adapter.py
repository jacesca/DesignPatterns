# -*- coding: utf-8 -*-
################################################
# Adapter
# ----------------------------------------------
# Getting the interface you want from the interface you have.
# An adapter is a construct which adapts an existing interface X to conform
# to the required interface Y.
# ----------------------------------------------
# Similar to electrical devices have different power (interface) requirements:
# - Voltage (5V, 220V).
# - Socket/plug type (Europe, UK, USA).
# We cannot modify our gadgets to support every possible interface.
# - Some support possible (e.g. 120/220V).
# Thus we yse a special device (an adapter) to give us the interface we require
# from the interface we have.
# ----------------------------------------------
# When an API does not match with what we want to do, an adapter can be constructed.
# ----------------------------------------------
# Summary:
# Implementing an adapter is easy.
# Determine the API you have and the API you need.
# Create a component which aggregates (has a reference to, ...) the adaptee.
# Intermediate representations can pile up: use caching and other optimizations.
################################################


# ----------------------------------------------
# you are given this
# ----------------------------------------------
class Point:
  def __init__(self, x, y) -> None:
    self.x = x
    self.y = y


def draw_point(p:Point) -> None:
  print('.', end='')



# ----------------------------------------------
# Objects required to draw:
# Problem: only points are drawed
# ----------------------------------------------
class Line:
  def __init__(self, start:Point, end:Point) -> None:
    self.start = start
    self.end = end


class Rectangle(list):
  """
  Re´resemted as a list of lines.
  """
  def __init__(self, x:float, y:float, width:float, height:float) -> None:
    super().__init__()
    self.append(Line(Point(x, y), Point(x+width, y)))
    self.append(Line(Point(x+width, y), Point(x+width, y+height)))
    self.append(Line(Point(x, y), Point(x, y+height)))
    self.append(Line(Point(x, y+height), Point(x+width, y+height)))


# ----------------------------------------------
# Creating an adapter without caching.
# In order to adapt a line to a point you have to generate lots of points. Why
# do we have to keep doing it over and over again?
# ----------------------------------------------
class LineToPointAdapter(list):
  """
  This adapter will help us to represent the lines as a serie of points.
  """
  count = 0

  def __init__(self, line:Line) -> None:
    LineToPointAdapter.count += 1
    print(f'{LineToPointAdapter.count}: Generating points for line: '
          f'[{line.start.x}, {line.start.y}] -> '
          f'[{line.end.x}, {line.end.y}]')

    left = min(line.start.x, line.end.x)
    right = max(line.start.x, line.end.x)
    top = max(line.start.y, line.end.y)
    bottom = min(line.start.y, line.end.y)

    if right - left == 0:
      for y in range (top, bottom):
        self.append(Point(left, y))
    elif top - bottom == 0:
      for x in range(left, right):
        self.append(Point(x, top))
    

def draw(rcs: list[Rectangle]):
  print('--- Drawing some stuff ---')
  for rc in rcs:
    for line in rc:
      adapter = LineToPointAdapter(line)
      for p in adapter:
        draw_point(p)


# ----------------------------------------------
# Creating an adapter with caching
# Optimize the problem raised in the no caching adapter.
# ----------------------------------------------
class LineToPointAdapterCashing():
  """
  This adapter will help us to represent the lines as a serie of points.
  Use caching.
  """
  count = 0
  cache = {}

  def __init__(self, line:Line) -> None:
    self.h = hash(line)
    if self.h in LineToPointAdapterCashing.cache:
      return

    LineToPointAdapterCashing.count += 1
    print(f'{LineToPointAdapterCashing.count} ({self.h}): Generating points for line: '
          f'[{line.start.x}, {line.start.y}] -> '
          f'[{line.end.x}, {line.end.y}]')

    left = min(line.start.x, line.end.x)
    right = max(line.start.x, line.end.x)
    top = max(line.start.y, line.end.y)
    bottom = min(line.start.y, line.end.y)

    points = []

    if right - left == 0:
      for y in range (top, bottom):
        points.append(Point(left, y))
    elif top - bottom == 0:
      for x in range(left, right):
        points.append(Point(x, top))

    LineToPointAdapterCashing.cache[self.h] = points

  def __iter__(self):
    return iter(LineToPointAdapterCashing.cache[self.h])


def draw_caching(rcs: list[Rectangle]):
  print('--- Drawing some stuff ---')
  for rc in rcs:
    for line in rc:
      adapter = LineToPointAdapterCashing(line)
      for p in adapter:
        draw_point(p)


if __name__ == '__main__':
  rcs = [
    Rectangle(1, 1, 10, 10),
    Rectangle(3, 3, 6, 6)
  ]

  print('Adapter (No caching)')
  draw(rcs)

  print('................................................')
  print('Adapter (with caching)')
  draw_caching(rcs)
