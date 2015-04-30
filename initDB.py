__author__ = 'Trevor'

import sqlite3
import feedparser

conn = sqlite3.connect('database.db')

c = conn.cursor()
# c.execute('''CREATE TABLE feeds (name text, url text)''')
# c.execute("INSERT INTO feeds VALUES('reddit', 'http://www.reddit.com/r/python/.rss')")
conn.commit()

t = ('reddit', )
ret = c.execute("SELECT url FROM feeds WHERE name=?", t)
queryReturn = c.fetchone()
if queryReturn:
    queryString = "%s %s" % (queryReturn[0], "")
print queryString
d = feedparser.parse(str(queryString))
print d['feed']['title']
c.close()
conn.close()
