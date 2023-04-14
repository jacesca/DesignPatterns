# -*- coding: utf-8 -*-
"""
Provides some examples related to the iterator design pattern.
"""
################################################
# List Backed Properties
################################################


class Creature:
    """
    Main problem with this class is that each time a new ability is added, 
    all the property methods needs to be updated.
    """
    def __init__(self):
        self.strength = 10
        self.agility = 10
        self.intelligence = 10

    @property
    def sum_of_stats(self):
        return self.strength + self.intelligence + self.agility

    @property
    def max_stat(self):
        return max(self.strength + self.intelligence + self.agility)

    @property
    def average_stat(self):
        return self.sum_of_stats / 3.0
      

class CreatureImproved:
    """
    An improved class of Creature, all the ability will be stored in an array.
    """
    _strength = 0
    _agility = 1
    _intelligence = 2
    
    def __init__(self):
        self.stats = [10, 10, 10]

    @property
    def strength(self):
      return self.stats[CreatureImproved._strength]

    @strength.setter
    def strength(self, value):
      self.stats[CreatureImproved._strength] = value

    @property
    def agility(self):
      return self.stats[CreatureImproved._agility]

    @agility.setter
    def agility(self, value):
      self.stats[CreatureImproved._agility] = value

    @property
    def intelligence(self):
      return self.stats[CreatureImproved._intelligence]

    @intelligence.setter
    def intelligence(self, value):
      self.stats[CreatureImproved._intelligence] = value

    @property
    def sum_of_stats(self):
        return sum(self.stats)

    @property
    def max_stat(self):
        return max(self.stats)

    @property
    def average_stat(self):
        return float(self.sum_of_stats) / len(self.stats)
    

if __name__ == '__main__':
    print('----------------------------------------------------------------------')
    print('Iterator pattern:')
    print('----------------------------------------------------------------------')
    
    print('----------------------------------------------------------------------')
  