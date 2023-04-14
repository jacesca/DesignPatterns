# -*- coding: utf-8 -*-
################################################
# Singleton Decorator
################################################


def singleton(class_):
  instances = {}
  
  def get_instance(*args, **kwargs):
    if class_ not in instances:
      instances[class_] = class_(*args, **kwargs)
    return instances[class_]
  
  return get_instance


@singleton
class Database:
  """
  With this decorator, we prevent the class gets called several times.
  """
  def __init__(self):
    print('Loading database')
    
    
if __name__ == '__main__':
  print('Testing the singleton decorator')
  print('................................................')
  d1 = Database()
  d2 = Database()
  
  print(d1 == d2)
  