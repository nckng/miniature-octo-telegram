import sqlite3
from collections import OrderedDict

def hasContributed(username, story):
    db = sqlite3.connect('data/bd.db')
    c = db.cursor()
    s = c.execute("SELECT * FROM '%s'"%(story))
    for entry in s:
        if entry[0] == username: return True
    return False

def genStory(title):
    story = OrderedDict()
    db = sqlite3.connect('data/bd.db')
    c = db.cursor()
    s = c.execute("SELECT * FROM '%s'"%(title))
    for entry in s:
        user = entry[0]
        text = entry[1]
        story[user] = text
    return story

def genAuthor(story):
    db = sqlite3.connect('data/bd.db')
    c = db.cursor()
    s = c.execute("SELECT * FROM '%s'"%(story))
    author = s.fetchone()[0]
    return author

def genLast(story):
    db = sqlite3.connect('data/bd.db')
    c = db.cursor()
    s = c.execute("SELECT * FROM '%s'"%(story))
    for r in s:
        entry = r
    user = entry[0]
    text = entry[1]
    return user + ": " + text
