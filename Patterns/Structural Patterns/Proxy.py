# -*- coding: utf-8 -*-
################################################
# Proxy
# ----------------------------------------------
# A structural design pattern that lets you provide a substitute 
# or placeholder for another object. A proxy controls access to the 
# original object, allowing you to perform something either before 
# or after the request gets through to the original object.
# An interface for accessing a particular resource.
# A class that functions as an interface to a particular resource.
# That resource may be remote, expensive to construct, or may require
# logging or some other added functionality.
# ----------------------------------------------
# Motivation:
# You are calling foo.Bar()
# This assumes that foo is the same process as Bar().
# What if, later on, you want to put all Foo-related operations into 
# a separate process. Can you avoid changing your code?
# Proxy is the solution for these cases. 
# Proxy can provide the same interface, but entirely different
# behaviour.
# This is called a communication proxy. Other types: logging, virtual, 
# guarding, ...
# ----------------------------------------------
# Proxy vs Decorator:
# (1) Proxy provides an identical interface; decorator provides an enhanced interface.
# (2) Decorator typically aggregates (or has reference to) what it is decorating; 
#     proxy doesn't have to.
# (3) Proxy might not even be working with a materialized object.
# ----------------------------------------------
# Summary:
# A proxy has the same interface as the underlying object.
# To create a proxy, simply replicate the existing interface of an object.
# Add relevant functionality to the redefined member functions.
# Different proxies (communication, logging, caching, etc.) have completely
# different behaviors.
################################################


if __name__ == '__main__':
  print('................................................')
  print('Just theory.')
  print('................................................')
  