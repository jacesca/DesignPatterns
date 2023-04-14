# -*- coding: utf-8 -*-
################################################
# Composite - Neural Networks
################################################
from abc import ABC
from collections.abc import Iterable


class Connectable(Iterable, ABC):   
  def connect_to(self, other):
    if self == other:
        return
      
    for s in self:
      for o in other:
        s.outputs.append(o)
        o.inputs.append(s)
    

class Neuron(Connectable):
  def __init__(self, name:str) -> None:
    self.name = name
    self.inputs = []
    self.outputs = []
    
  
  def __str__(self) -> str:
    return f'{self.name}, ' \
           f'{len(self.inputs)} inputs, ' \
           f'{len(self.outputs)} outputs'
           
  def __iter__(self) -> None:
    yield self
           
  # def connect_to(self, other:Neuron) -> None:
  #   """
  #   Only works for Neuron objects and not for NeuronLayers.
  #   """
  #   self.outputs.append(other)
  #   other.inputs.append(self)


class NeuronLayer(list, Connectable):
  def __init__(self, name: str, count: int) -> None:
    super().__init__()
    self.name = name
    for x in range(count):
      self.append(Neuron(f'{name}-{x}'))
      
  def __str__(self) -> str:
    return f'{self.name} with {len(self)} neurons'


# def connect_to(self, other):
#   """
#   Classes are always the best option.
#   """
#   if self == other:
#     return
  
#   for s in self:
#     for o in other:
#       s.outputs.append(o)
#       o.inputs.append(s)
  
  
if __name__ == '__main__':
  neuron1 = Neuron('n1')
  neuron2 = Neuron('n2')
  
  layer1 = NeuronLayer('L1', 3)
  layer2 = NeuronLayer('L2', 4)
  
  
  # Neuron.connect_to = connect_to
  # NeuronLayer.connect_to = connect_to
  
  neuron1.connect_to(neuron2)
  neuron1.connect_to(layer1)
  layer1.connect_to(neuron2)
  layer1.connect_to(layer2)
  
  print('Composite - Neuron Network Example')
  print('................................................')
  print(neuron1)
  print(neuron2)
  print(layer1)
  print(layer2)
  print(layer1[0])
  