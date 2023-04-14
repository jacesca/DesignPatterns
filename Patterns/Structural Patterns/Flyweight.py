# -*- coding: utf-8 -*-
################################################
# Flyweight
# ----------------------------------------------
# A structural design pattern that lets you fit more objects 
# into the available amount of RAM by sharing common parts of 
# state between multiple objects instead of keeping all of 
# the data in each object.
# Space optimization.
# A space optimization techniquee that lets us use less memory
# by storing externally the data associated with similar objects.
# ----------------------------------------------
# Motivation:
# Avoid redundancy when storing data.
# E.g. MMORPG (Massively multiplayer online role-playing games)
# - Plenty of users with identical first/last names.
# - No sense in storing same first/last name over and over again.
# - store a list of names and references to them.
# E.g. Bold or Italic text formatting
# - Don't want each character to have a formatting character.
# - Operates on ranges (e.g. line number, start/end positions).
# ----------------------------------------------
# Summary:
# Store common data externally.
# Specify an index or a references into the external data store.
# Define the idea of ranges on homogeneous collections and 
# store data related to those ranges.
################################################


if __name__ == '__main__':
  print('................................................')
  print('Just theory.')
  print('................................................')
  