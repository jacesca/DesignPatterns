# -*- coding: utf-8 -*-
################################################
# Visitor
# ----------------------------------------------
# A behavioral design pattern that lets you separate algorithms 
# from the objects on which they operate.
# Allow adding extra behaviors to entire hierarchies of classes.
# A component (visitor) that knows how to traverse a data structure
# composed of (possible related) types.
# ----------------------------------------------
# Motivation:
# Need to define a new operation on an entire class hierarchy:
# - E.g. make a document model printable to HTML/Markdown.
# Do not want to keep modifying every class in the hierarchy.
# Need access to the non-common aspects of classes in the hierarchy.
# Create an external component to handle rendering:
# - But avoid explicit type checks.
# ----------------------------------------------
# Summary:
# - OOP double-dispatch approach is not necessary in Python.
#   (related to the accept method implemented in the classic approach).
# - Make a visitor, decorating each 'overload' with @visitor.
# - Call visit() and the entire structure gets traversed.
################################################

    
# ----------------------------------------------
# Intrusive approach. Alter the OCP.
# ----------------------------------------------
class DoubleExpression:
    def __init__(self, value):
        self.value = value
    
    def print(self, buffer):
        buffer.append(str(self.value))
        
    def eval(self):
        return self.value
        
class AdditionExpression:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def print(self, buffer):
        buffer.append('(')
        self.left.print(buffer)
        buffer.append(' + ')
        self.right.print(buffer)
        buffer.append(')')
        
    def eval(self):
        return self.left.eval() + self.right.eval()
    
if __name__ == '__main__':
    print('................................................')
    print('Intrusive Visitor pattern:')
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
    e.print(buffer)
    print(''.join(buffer), ' = ', e.eval())
    