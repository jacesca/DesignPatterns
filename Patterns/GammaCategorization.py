# -*- coding: utf-8 -*-
################################################
# GAMMA CATEGORIZATION
# ----------------------------------------------
# Design patterns are typically split into 3 categories:
# ----------------------------------------------
# - Creational Patterns:
#   Deal with the creation (construction) of objects.
#   Explicit (constructor) vs implicit (DI, reflection, etc.).
#   Wholesale (single statement) vs piecewise (step-by-step).
#     * Factory Method.
#     * Abstract Factory.
#     * Builder.
#     * Prototype.
#     * Singleton.
#     * Monostate.
# ----------------------------------------------
# - Structural Patterns:
#   Concerned with the structure (e.g., class members).
#   Many patterns are weappers that mimic the underlying class' interface.
#   Stress the importance of good API design.
#     * Adapter.
#     * Bridge.
#     * Composite.
#     * Decorator.
#     * Facade.
#     * Flyweight.
#     * Proxy.
# ----------------------------------------------
# - Behavioral Patterns:
#   They are different, no central theme.
#     * Chain of Responsability.
#     * Command.
#     * Memento.
#     * Observer.
#     * Template Method.
#     * Visitor.
#     * Iterator.
#     * Mediator.
#     * State.
#     * Strategy.
#     * Interpreter.
# ----------------------------------------------
# Source: https://refactoring.guru/design-patterns/catalog
################################################

if __name__ == '__main__':
  print('Design Patterns')
  
# ----------------------------------------------
# - Creational Patterns:
#     * Factory Method          : Factory method more expresive than initializer.
#                                 Factory can be an outside class or inner class.
#     * Abstract Factory.
#     * Builder                 : Separate component for when object constuction 
#                                 gets too complicated.
#                                 Can create mutually cooperating sub builders.
#                                 Often has a fluent interface.
#     * Prototype               : Creation of object from an existing object.
#                                 Requires explicit deep copy.
#     * Singleton               : When you need to ensure just a single instance
#                                 exists.
#                                 Easy to make with a decorator or metaclass.
#                                 Consider using dependency injection.
#     * Monostate.
# ----------------------------------------------
# - Structural Patterns:
#     * Adapter                 : Converts the interface you get to the interface
#                                 you need.
#     * Bridge                  : Decouple abstraction from implementation.
#     * Composite               : Allos clients to treat individual objects and
#                                 compositions of object uniformly.
#     * Decorator:              : Attach additional responsabilities to objects.
#                                 Python has functional decorators.
#     * Facade                  : Provide a single unified interface over a set of
#                                 interfaces.
#                                 Friendly and easy to use, but can provide access
#                                 to low level features.
#     * Flyweight               : Efficiently support very large numbers of similar
#                                 objects.
#     * Proxy                   : Provide a urrogate object that forwards calls to
#                                 the real object while performing additional 
#                                 functions.
#                                 E.g. access control, communication, logging, etc.
# ----------------------------------------------
# - Behavioral Patterns:
#     * Chain of Responsability : Allow components to process information/events
#                                 in a chain.
#                                 Each element in the chain refers to next element,
#                                 or make a list and go through it.
#     * Command                 : Encapsulate a request into a separete object.
#                                 Good for audit, replay, undo/redo.
#                                 Part of CQS/CQRS.
#                                 CQS ---> Command Query Separation
#                                 CQRS --> Command Query Responsibility Segregation
#                                          Part of interprise patterns.
#     * Memento                 : Yields tokens representing system states.
#                                 Tokens do not allow direct manipulation, but can
#                                 be used in appropriate APIs.
#     * Observer                : Allows notification of changes/happening in a
#                                 component.
#     * Visitor                 : Allows non intunsive addition of functionality
#                                 to hierarchies.
#     * Iterator                : Provides an interface for accessing elements of
#                                 an aggreaget obbject.
#                                 __iter__ / __next__ are stateful, but yield is
#                                 much more convenient.
#     * Mediator                : Provides mediation services between two objects.
#                                 E.g. message passing, chat room.
#     * State                   : We model systems by having one of a possible states
#                                 and transitions between these states.
#                                 Such a system is called a state machine.
#                                 Special frameworks exists to orchestrate state
#                                 machine.
#     * Strategy & Template     : Both define a skeleton algorithm with details filled
#                                 in by implementor.
#                                 Strategy uses ordinary composition template method
#                                 uses inheritance.
#     * Template Method.
#     * Interpreter             : Transform textual input into object-oriented
#                                 structures.
#                                 Used by interpreters, compilers, static analysis
#                                 tools, etc.
#                                 Compiler Theory is a separate branch of Computer
#                                 Science.
# ----------------------------------------------
