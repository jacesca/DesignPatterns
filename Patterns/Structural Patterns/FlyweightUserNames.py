# -*- coding: utf-8 -*-
################################################
# Flyweights Decorator | Usernames example
################################################
import string, random


class User:
  def __init__(self, name: str) -> None:
    self.name = name
    
  def __str__(self) -> str:
    return self.name
  
  def __repr__(self) -> str:
    return f'User({self.name})'
    

def random_string():
  chars = string.ascii_lowercase
  return ''.join(
    [random.choice(chars) for _ in range(8)]
  )


# Optimizing the class
class UserOptimized:
  strings = []
  
  def __init__(self, full_name:str) -> None:
    def get_or_add(s):
      if s in self.strings:
        return self.strings.index(s)
      else:
        self.strings.append(s)
        return len(self.strings) - 1
      
    self.names = [get_or_add(n) for n in full_name.split(' ')]
    
  def __str__(self) -> str:
    return ' '.join([self.strings[n] for n in self.names])
  
  def __repr__(self) -> str:
    return f'User({self.__str__()})'
  

if __name__ == '__main__':
  print('................................................')
  print('User names example:')
  
  size = 100
  first_names = [random_string() for _ in range(size)]
  last_names = [random_string() for _ in range(size)]
  users = [User(f'{fn} {ln}') for fn in first_names for ln in last_names]
  print(users[:10])
  
  print('................................................')
  print('User names applying the Flyweights pattern:')
  
  size = 100
  first_names = [random_string() for _ in range(size)]
  last_names = [random_string() for _ in range(size)]
  users = [UserOptimized(f'{fn} {ln}') for fn in first_names for ln in last_names]
  print(users[:10])
  
  print('................................................')
