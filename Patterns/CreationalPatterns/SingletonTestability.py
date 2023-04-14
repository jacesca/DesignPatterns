# -*- coding: utf-8 -*-
################################################
# Singleton Testability
################################################
import os, sys
from unittest import TestCase, main


class Singleton(type):
  _instances = {}
  
  def __call__(cls, *args, **kwds):
    if cls not in cls._instances:
      cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwds)
    return cls._instances[cls]


class Database(metaclass=Singleton):
  def __init__(self):
    self.population = {}
    with open(os.path.join(sys.path[0], 'capitals.txt'), 'r') as f:
      lines = f.readlines()
    
    for i in range(0, len(lines), 2):
      self.population[lines[i].strip()] = int(lines[i+1].strip())


class SingletonRecordFinder:
  """As we call Database(), we instantiate the DB if no one has ready it yet."""
  def total_population(self, cities):
    result = 0
    for c in cities:
      result += Database().population[c]
    return result


class ConfigurableRecordFinder:
  def __init__(self, db):
    self.db = db
    
  def total_population(self, cities):
    result = 0
    for c in cities:
      result += self.db.population[c]
    return result


class DummyDatabase:
  population = {
    'alpha': 1,
    'beta': 2,
    'gamma': 3,
  }
  
  def get_population(self, name):
    return self.population[name]


class TestSingleton(TestCase):
  ddb = DummyDatabase()
  
  def test_is_singleton(self):
    db1 = Database()
    db2 = Database()
    self.assertEqual(db1, db2)
    
  def test_singleton_total_population(self):
    """
    The risk with this implemented class is that for 
    test case we can not replace the current live database.
    """
    rf = SingletonRecordFinder()
    names = ['Seoul', 'Mexico City']
    tp = rf.total_population(names)
    self.assertEqual(tp, 17500000+17400000) 
    
  def test_configurable_record_finder(self):
    """
    This method included in the test has a better approach
    because we can define a dummy database instead of live database.
    """
    crf = ConfigurableRecordFinder(self.ddb)
    self.assertEqual(3, crf.total_population(['alpha', 'beta']))


if __name__ == '__main__':
    main() 
  