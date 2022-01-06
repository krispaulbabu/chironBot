from re import sub
import praw
import time
import threading
from datetime import datetime
from praw.reddit import Comment

reddit= praw.Reddit(
    client_id="xH6yTQBCYsiOL_fEyDDokQ",
    client_secret="pbiL_xG6AUr10G163T1SsA5inNavyw",
    user_agent="TesterBott",
    username="tester_bot79",
    password="kriswashere"
)
def makeAComment(aPost):
  aPost.reply("Chiron")
  print("I've made a comment")

# Just a comment to check if pushing works.

while(True):
  allSubmission=[]
  subreddit=reddit.subreddit("samplecommfortest")
  i=0
  for submission in subreddit.hot():
    allSubmission.append(submission)
    i+=1
    if i==100:
      break
  makeAComment(allSubmission[0])
  time.sleep(10)

