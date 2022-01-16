import sqlite3

def printAll():
  for row in cur.execute('''select * from temp_info'''):
    print(row)

def insert(post, comment):
  cur.execute("insert into temp_info values("+''' " '''+post+''' "," '''+
    comment+ ''' ") ''')

con=sqlite3.connect("database.db")
cur=con.cursor()

insert("post_1","comment_1")
printAll()

con.commit()

