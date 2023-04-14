# -*- coding: utf-8 -*-
################################################
# Reflective Visitor
################################################
from abc import ABC


class Expression(ABC):
    pass

    
class DoubleExpression(Expression):
    def __init__(self, value):
        self.value = value
        
class AdditionExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        

class ExpressionPrinter:
    @staticmethod
    def print(expression, buffer):
        if isinstance(expression, DoubleExpression):
            buffer.append(str(expression.value))
        elif isinstance(expression, AdditionExpression):
            buffer.append('(')
            ExpressionPrinter.print(expression.left, buffer)
            buffer.append(' + ')
            ExpressionPrinter.print(expression.right, buffer)
            buffer.append(')')

    @staticmethod
    def eval(expression):
        if isinstance(expression, DoubleExpression):
            return expression.value
        elif isinstance(expression, AdditionExpression):
            return ExpressionPrinter.eval(expression.left) + \
                   ExpressionPrinter.eval(expression.right)
            
    Expression.print = lambda self, b: ExpressionPrinter.print(self, b)
    Expression.eval = lambda self: ExpressionPrinter.eval(self)
                   
                   
                   
if __name__ == '__main__':
    print('................................................')
    print('Reflective Visitor pattern:')
    print('................................................')
    print("""
    #   The problem:
    #   Read expressions to print/evaluate them. 
    #   Expressions will include only addition or substraction operation.
    #   Expression will look like this:
    #       1 + (2 + 3)
    """)
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    
    buffer = []
    ExpressionPrinter.print(e, buffer)
    print(''.join(buffer), ' = ', ExpressionPrinter.eval(e))
    
    buffer = []
    e.print(buffer)
    print(''.join(buffer), ' = ', e.eval())
