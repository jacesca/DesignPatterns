# -*- coding: utf-8 -*-
################################################
# Dynamic Decorator
################################################
class FileWithLogging:
  def __init__(self, file):
    self.file = file
  
  def writelines(self, strings):
    self.file.writelines(strings)
    print(f'wrote {len(strings)} lines')
  
  # dynamic code
  # whatever other calls, they were proxy over to underlying file methods.
  # penalty: performace cost, in each call this dynamic processing time will be added it.
  # this avoid to create each method as follow:
  # # def write(self, item):
  # #   self.file.write(item)
    
  def __iter__(self):
    return self.file.__iter__()
  
  def __next__(self):
    return self.file.__next__()

  def __getattr__(self, item):
    return getattr(self.__dict__['file'], item)

  def __setattr__(self, key, value):
    if key == 'file':
      self.__dict__[key] = value
    else:
      setattr(self.__dict__['file'], key)
      
  def __delattr__(self, item):
    delattr(self.__dict__['file'], item)

if __name__ == '__main__':
  print('................................................')
  print('Writing a file:')
  
  file_name = 'hello.txt'
  file = FileWithLogging(open(file_name, 'w'))
  file.writelines(['Hello!\n', 'Here is my file.\n', 'Bye.\n'])
  file.write('Adding a new line.')
  file.close()
  
  print('................................................')
  print('Reading the created file:')
  with open(file_name) as f:
    print(f.read())
    
  print('................................................')
