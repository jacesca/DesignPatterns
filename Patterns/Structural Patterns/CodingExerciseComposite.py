# -*- coding: utf-8 -*-
################################################
# Composite Coding Exercise
# ----------------------------------------------
# Consider the code presented below. We have two classes called 
# SingleValue and ManyValues. SingleValue stores just one numeric 
# value, but ManyValues can store either numeric values or 
# SingleValue objects.
# You are asked to give both SingleValue and ManyValues a property 
# member called sum that returns a sum of all the values that the 
# object contains. Please ensure that there is only a single method 
# that realizes the property sum, not multiple methods.
# Here is a sample unit test:
#    class FirstTestSuite(unittest.TestCase):
#        def test(self):
#            single_value = SingleValue(11)
#            other_values = ManyValues()
#            other_values.append(22)
#            other_values.append(33)
#            # make a list of all values
#            all_values = ManyValues()
#            all_values.append(single_value)
#            all_values.append(other_values)
#            self.assertEqual(all_values.sum, 66) 
################################################
from unittest import TestCase, main
from abc import ABC
from collections.abc import Iterable


class Summable(Iterable, ABC):   
  @property
  def sum(self):
    #return sum([item for item_list in self for item in item_list])
    result = 0
    for item_list in self:
      for item in item_list:
        result += item
        
    return result


class SingleValue(Summable):
  def __init__(self, value):
      self.value = value
        
  def __iter__(self):
      yield self.value


class ManyValues(list, Summable):
  pass

  
class TestFirstSuite(TestCase):
  def test(self):
    single_value = SingleValue(11)
    other_values = ManyValues()
    other_values.append(22)
    other_values.append(33)
    
    # make a list of all values
    all_values = ManyValues()
    all_values.append(single_value)
    all_values.append(other_values)
    self.assertEqual(all_values.sum, 66)
      
      
if __name__ == '__main__':
  main() 