from ctypes import sizeof
from praw.reddit import Comment
import random

from numpy import size
from sympy import linear_eq_to_matrix

def returnLine(comment):
  number=random.randrange(0,size(lines))
  line=lines[number]
  line=line.replace("u/Author","u/"+str(comment.author))
  return line


# Method to replace name with author's name 
lines=[
  "Im sure the boy can learn", 
  "Ah, good, u/Author, now we have four for Pinochle",
  "I must say Percy, Im glad to see you alive"
  ]

