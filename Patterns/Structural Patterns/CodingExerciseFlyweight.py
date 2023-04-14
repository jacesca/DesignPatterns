# -*- coding: utf-8 -*-
################################################
# Flyweight Coding Exercise
# ----------------------------------------------
# You are given a class called Sentence, which takes a 
# string such as 'hello world'. You need to provide an 
# interface such that the indexer returns a flyweight that 
# can be used to capitalize a particular word in the sentence.
# Typical use would be something like:
#     sentence = Sentence('hello world')
#     sentence[1].capitalize = True
#     print(sentence)  # writes "hello WORLD"
################################################
from unittest import TestCase, main


class Sentence:
  def __init__(self, plain_text:str) -> None:
    self.plain_text = plain_text
    self.words = plain_text.split(' ')
    self.tokens = {}
    
  def __getitem__(self, item: int) -> bool:
    word_token = self.WordToken()
    self.tokens[item] = word_token
    # print(self.tokens)
    return self.tokens[item]
  
  
  class WordToken:
    def __init__(self, capitalize: bool=False) -> None:
      self.capitalize = capitalize
      
    def __repr__(self):
        return str(self.capitalize)


  def __str__(self) -> str:
    result = []
    for i in range(len(self.words)):
      w = self.words[i]
      if i in self.tokens and self.tokens[i].capitalize:
        w = w.upper()
      result.append(w)
    return ' '.join(result)


class Evaluate(TestCase):
    def test_exercise(self):
        s = Sentence('alpha beta gamma')
        s[1].capitalize = True
        self.assertEqual(str(s), 'alpha BETA gamma')
        
        
if __name__ == '__main__':
  main() 
