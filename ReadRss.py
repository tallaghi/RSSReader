__author__ = 'tallaghi'
import feedparser
import sqlite3


class DatabaseOperations():
    def __init__(self):
        self.conn = sqlite3.connect('database.db', timeout=10)
        self.c = self.conn.cursor()
       #self.c.execute("insert into feeds values('tattoo', 'http://www.reddit.com/r/tattoo/.rss')")
        self.conn.commit()
    def getOne(self, input):
        t = (str(input), )
        print t
        ret = self.c.execute("SELECT url FROM feeds WHERE name=?", t)
        queryReturn = self.c.fetchone()
        print queryReturn
        if queryReturn:
            queryString = "%s %s" % (queryReturn[0], "")
        d = feedparser.parse(str(queryString))
        testReturn=[]
        for e in d.entries:
            dic = {'title': str(e.title), 'link': str(e.link), 'feed': str(d.feed.title), 'time': e.published}
            testReturn.append(dic)
        print testReturn
        return testReturn

    def getAll(self):
        ret=self.c.execute("select name from feeds")
        queryReturn = self.c.fetchall()
        rssList=[]
        for each in queryReturn:
            query = "%s %s" % (each[0], "")
            print str(query.rstrip())
            rssList += self.getOne(query.rstrip())
        print rssList
        return rssList

    def addFeed(self, feed, feedName):
        self.c.execute("insert into feeds values(?, ?)", (feedName, feed))
        self.conn.commit()

    def removeFeed(self, feedName):
        self.c.execute("delete from feeds where name = ?", (feedName,))

    def close(self):
        self.c.close()
        self.conn.close()


t = DatabaseOperations()
t.getOne('xkcd')
t.close()
