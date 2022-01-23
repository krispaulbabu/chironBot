from re import sub
from string import printable
import praw
import time
from datetime import datetime
from praw.reddit import Comment
from picker import *

import psutil
import threading

reddit= praw.Reddit(
    client_id="X430vgp1j67BatZ-aHjxqw",
    client_secret="QBLYkz-RzYstXpNtTjRTSJRVI0wdRw",
    user_agent="Abott",
    username="sample_bot79",
    password="kriswashere"
)

def getPosts(listOfPosts):
  i=0
  for post in listOfPosts:
    i+=1
    aPost=reddit.submission(id=post.id)
    aPost.comments.replace_more(limit=None)
    for comment in aPost.comments:
      scrollThru(comment,"-")
    time.sleep(5)

def scrollThru(comment,aTab):
  if(checkChiron(comment) and not replied(comment)):
    comment.reply(returnLine(comment))
    comment.save()
    time.sleep(2)
  if(len(comment.replies)!=0):
    for reply in comment.replies:
      aType=type(reply).__name__
      aTab+="-"
      scrollThru(reply,aTab)

def checkChiron(comment):
  if "chiron" in comment.body or "Chiron" in comment.body:
    return 1
  return 0

def replied(comment):
  if(comment.author=="sample_bot79"):
    return 1
  if(comment.saved):
    return 1
  return 0
  

while(True):
  allSubmission=[]
  subreddit=reddit.subreddit("samplecommfortest")
  i=0
  for submission in subreddit.hot():
    allSubmission.append(submission)
    i+=1
    if i==100:
      break
  getPosts(allSubmission)
  time.sleep(3)