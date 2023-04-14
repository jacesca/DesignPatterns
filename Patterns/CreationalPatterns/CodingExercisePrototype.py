# -*- coding: utf-8 -*-
################################################
# Prototype Coding Exercise
# ----------------------------------------------
# Given the definitions shown in code, you are asked to implement Line.deep_copy()  
# to perform a deep copy of the given Line  object. 
# This method should return a copy of a Line that contains copies of its start/end points.
# Note: please do not confuse deep_copy() with __deepcopy__()!
################################################
from copy import deepcopy
from unittest import TestCase, main


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end
    
    def deep_copy(self):
        return deepcopy(self)
      

class TestEvaluate(TestCase):
    def test_exercise(self):
        line1 = Line(
            Point(3, 3),
            Point(10, 10)
        )
        line2 = line1.deep_copy()
        line1.start.x = line1.end.x = line1.start.y = line1.end.y = 0

        self.assertEqual(3, line2.start.x)
        self.assertEqual(3, line2.start.y)
        self.assertEqual(10, line2.end.x)
        self.assertEqual(10, line2.end.y)
        

if __name__ == '__main__':
    main()     
    