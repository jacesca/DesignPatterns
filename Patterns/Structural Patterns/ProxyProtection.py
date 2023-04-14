# -*- coding: utf-8 -*-
################################################
# Protection Proxy
################################################
class Driver:
  def __init__(self, name: str, age: int) -> None:
    self.name = name
    self.age = age


class Car:
  def __init__(self, driver: Driver) -> None:
    self.driver = driver
    
  def drive(self) -> None:
    print(f'Car is being driven by {self.driver.name}')


# Adding the proxy pattern
class CarProxy:
  def __init__(self, driver: Driver) -> None:
    self.driver = driver
    self._car = Car(driver)

  def drive(self) -> None:
    if self.driver.age >= 16:
      self._car.drive()
    else:
      print('Driver too young!')
  
if __name__ == '__main__':
  print('................................................')
  print('The objects:')
  
  driver = Driver('John', 45)
  car = Car(driver)
  car.drive()
  
  print('................................................')
  print('Applying the Proxy pattern:')
  
  driver = Driver('John', 15)
  car = CarProxy(driver)
  car.drive()
  
  print('................................................')
  