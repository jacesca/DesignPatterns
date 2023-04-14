# -*- coding: utf-8 -*-
################################################
# State
# ----------------------------------------------
# A behavioral design pattern that lets you define a family of 
# algorithms, put each of them into a separate class, and make 
# their objects interchangeable.
# Enables the exact behavior of a system to be selected at
# run-time.
# System behavior partially specified at runtime.
# ----------------------------------------------
# Motivation:
# Many algorithms can be decomposed into higher- and lower- level
# parts.
# Making tea can be decomposed into:
# - The process of making hot beverage (boil water, pour into cup), and
# - Tea-specific things (put teabag into water).
# The high level algorithm can then be reused for making coffe or hot
# chocolate.
# - Supported by beverage-specific strategies.
# ----------------------------------------------
# Summary:
# - Define an algorith at a high level.
# - Define the interface you expect each strategy to follow.
# - Provide for dynamic composition of strategies in the resulting objects.
################################################
from abc import ABC
from enum import Enum, auto


class ListStrategy(ABC):
    def start(self, buffer): pass
    def end(self, buffer): pass
    def add_list_item(self, buffer, item): pass


class MarkdownListStrategy(ListStrategy):
    def add_list_item(self, buffer, item):
        buffer.append(f' * {item}\n')
    
        
class HtmlListStrategy(ListStrategy):
    def start(self, buffer):
        buffer.append('<ul>\n')
    
    def end(self, buffer):
        buffer.append('</ul>\n')
        
    def add_list_item(self, buffer, item):
        buffer.append(f'  <li>{item}</li>\n')


class OutputFormat(Enum):
    MARKDOWN = auto()
    HTML = auto()


class TextPRocessor:
    def __init__(self, list_strategy=HtmlListStrategy):
        self.list_strategy = list_strategy
        self.buffer = []
        
    def append_list(self, items):
        self.list_strategy.start(self.buffer)
        for item in items:
            self.list_strategy.add_list_item(self.buffer, item)
        self.list_strategy.end(self.buffer)
        
    def set_output_format(self, format):
        if format == OutputFormat.MARKDOWN:
            self.list_strategy = MarkdownListStrategy()
        elif format == OutputFormat.HTML:
            self.list_strategy = HtmlListStrategy()
    
    def clear(self):
        self.buffer.clear()
        
    def __str__(self):
        return ''.join(self.buffer)
    
    
if __name__ == '__main__':
    print('................................................')
    print('Strategy pattern:')
    print('................................................')
    items = ['foo', 'bar', 'baz']
    tp = TextPRocessor()
    tp.set_output_format(OutputFormat.MARKDOWN)
    tp.append_list(items)
    print(tp)
    
    tp.set_output_format(OutputFormat.HTML)
    tp.clear()
    tp.append_list(items)
    print(tp)
    