import praw
import time
import threading
from datetime import datetime

from praw.reddit import Comment

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
    print(i,")","Post->",post.permalink)
    aPost=reddit.submission(id=post.id)
    # if(i==3):
    for comment in aPost.comments:
      scrollThru(comment,"-")
  
def scrollThru(comment,aTab):
  print(aTab,comment.body)
  if(len(comment.replies)!=0):
    for reply in comment.replies:
      aTab+="-"
      scrollThru(reply,aTab)

def checkChiron(comment):
  if "Chiron" in comment.body or "chiron" in comment.body:
    return 1
  return 0

def replied(comment):
  for reply in comment.replies:
    if reply.author=="sample_bot79":
      return 1
  return 0

while(True):
  allSubmission=[]
  subreddit=reddit.subreddit("dankmemes")
  i=0
  for submission in subreddit.hot():
    allSubmission.append(submission)
    i+=1
    if i==3:
      break
  getPosts(allSubmission)
  time.sleep(5)