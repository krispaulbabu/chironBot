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
  "Im sure the boy can learn", 
  "Ah, good, u/Author, now we have four for Pinochle",
  "I must say Percy, Im glad to see you alive",
  "What you learn from me, is vitally important. I expect you to treat it as such. I will accept only the best from you, u/Author.",
  "What ho, u/Author!",
  "Ah, that would be my pen. Please bring your own writing utensil in the future, u/Author",
  "We would only make matters worse by rushing him, We need the boy to mature more.",
  "Nothing, My nerves haven't been right since the winter solstice."
  ]

