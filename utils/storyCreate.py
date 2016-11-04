import sqlite3

def storyExists(story, c):
    s = c.execute('SELECT name FROM stories')
    for r in s:
        name = r[0]
        if story == name:
            return True;
    return False;

def addStory():
    
