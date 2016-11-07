import sqlite3
from collections import OrderedDict

def storyCount():
    db = sqlite3.connect('data/bd.db')
    c = db.cursor()
    s = c.execute("SELECT * FROM stories")
    if (s.fetchone() == None):
        return True
    return False

def getContent(story, db):
    content = []
    c = db.cursor()
    s = c.execute("SELECT * FROM '%s'"%(story))
    for entry in s:
        content.append([entry[0], entry[1]])
    return content

# returns True if user has contributed/authored specified story; false otherwise
def hasContributed(username, story, db):
    c = db.cursor()
    s = c.execute("SELECT * FROM '%s'"%(story))
    for entry in s:
        if entry[0] == username: return True
    return False

# returns True if user has contributed/authored > 0 stories; false otherwise
def hasContributedAny(username):
    db = sqlite3.connect('data/bd.db')
    c = db.cursor()
    s = c.execute("SELECT * FROM stories")
    for record in s:
        story = record[0]
        if hasContributed(username, story, db) == True:
            return True
        else: pass
    return False

# returns True if user has contributed/authored all exisiting stories; false otherwise
def hasContributedAll(username):
    db = sqlite3.connect('data/bd.db')
    c = db.cursor()
    s = c.execute("SELECT * FROM stories")
    for record in s:
        story = record[0]
        if hasContributed(username, story, db) == False:
            return False
        else: pass
    return True


# for stories you've contributed to
def myStoryList(username):
    stories = OrderedDict()
    db = sqlite3.connect('data/bd.db')
    c = db.cursor()
    s = c.execute("SELECT * FROM stories")
    for record in s:
        story = record[0]
        if hasContributed(username, story, db) == True:
            content = getContent(story, db)
            stories[story] = content
        else: pass
    return stories

# for stories you haven't contributed to
def nonStoryList(username):
    stories = OrderedDict()
    db = sqlite3.connect('data/bd.db')
    c = db.cursor()
    s = c.execute("SELECT * FROM stories")
    for record in s:
        story = record[0]
        if hasContributed(username, story, db) == False:
            content = getContent(story, db)
            stories[story] = content
        else: pass
    return stories

print storyCount()
