from ctypes import sizeof
from praw.reddit import Comment
import random

from numpy import size

def returnLine(comment):
  number=random.randrange(0,size(lines))
  line=lines[number]
  line=line.replace("u/Author","u/"+str(comment.author))
  return line


# Method to replace name with author's name 
lines=[
  "Fuck you u/Author"
  ]

