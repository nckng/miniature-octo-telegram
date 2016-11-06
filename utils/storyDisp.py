import sqlite3
from collections import OrderedDict

def hasContributed(username, story):
    db = sqlite3.connect('data/bd.db')
    c = db.cursor()
    s = c.execute('SELECT * FROM "%s"'%(story))
    for entry in s:
        if entry[0] == username: return True
    return False

def genStory(story):
    story = OrderedDict()
    db = sqlite3.connect('data/bd.db')
    c = db.cursor()
    s = c.execute('SELECT * FROM "%s"'%(story))
    for entry in s:
        user = entry[0]
        text = entry[1]
        story[user] = text
    return story

def genAuthor(story):
    db = sqlite3.connect('data/bd.db')
    c = db.cursor()
    s = c.execute('SELECT * FROM "%s"'%(story))
    author = "penis"
    return author

def genLast(story):
    db = sqlite3.connect('data/bd.db')
    c = db.cursor()
    s = c.execute('SELECT * FROM "%s" WHERE user = (SELECT MAX(user) FROM "%s")'%(story, story))
    entry = s.fetchone()
    user = entry[0]
    text = entry[1]
    return user + ": " + text
