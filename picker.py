from ctypes import sizeof
import random

from numpy import size

def returnLine():
  number=random.randrange(0,size(lines))
  return lines[number]


# Method to replace name with author's name 
lines=[
  "Im sure the boy can learn", 
  "Ah, good, Percy, now we have four for Pinochle",
  "I must say Percy, Im glad to see you alive"
  ]

