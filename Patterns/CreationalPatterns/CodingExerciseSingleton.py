# -*- coding: utf-8 -*-
################################################
# Singleton Coding Exercise
# ----------------------------------------------
# Since implementing a singleton is easy, you have a different 
# challenge: write a function called is_singleton(). 
# This method takes a factory method that returns an object and 
# it's up to you to determine whether or not that object is a 
# singleton instance.
################################################
from copy import deepcopy
from unittest import TestCase, main


def is_singleton(factory):
    obj1 = factory()
    obj2 = factory()
    
    return obj1 is obj2
        

class Evaluate(TestCase):
    def test_exercise(self):
        obj = [1, 2, 3]
        self.assertTrue(is_singleton(lambda: obj))
        self.assertFalse(is_singleton(lambda: deepcopy(obj)))
        
        
if __name__ == '__main__':
    main()     
    