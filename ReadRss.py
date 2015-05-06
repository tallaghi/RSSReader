__author__ = 'tallaghi'
import feedparser
import sqlite3


class DatabaseOperations():
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.c = self.conn.cursor()
        self.c.execute("insert into feeds values('tattoo', 'http://www.reddit.com/r/tattoo/.rss')")
        self.conn.commit()
    def getOne(self, input):
        t = (str(input), )
        ret = self.c.execute("SELECT url FROM feeds WHERE name=?", t)
        queryReturn = self.c.fetchone()
        if queryReturn:
            queryString = "%s %s" % (queryReturn[0], "")
        d = feedparser.parse(str(queryString))
        testReturn=[]
        for e in d.entries:
            testReturn.append(e.title)
        return testReturn
        self.c.close()
        self.conn.close()
    def getAll(self):
        ret=self.c.execute("select url from feeds")
        queryReturn=self.c.fetchall()
        tempList=[]
        for each in queryReturn:
            queryString = "%s %s" % (each[0], "")
            tempList.append(queryString)
        feedList=[]
        for entries in tempList:
            feedList.append(feedparser.parse(str(entries)))
        testReturn=[]
        for e in feedList:
            for x in e.entries:
                testReturn.append(x.title)
        return testReturn
        self.c.close()
        self.conn.close()


t = DatabaseOperations()
t.getAll()