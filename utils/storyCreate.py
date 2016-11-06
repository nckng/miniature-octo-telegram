import sqlite3

def storyExists(title, c):
    s = c.execute('SELECT name FROM stories')
    for r in s:
        name = r[0]
        if title == name:
            return True;
    return False;

def addStory(title, user, addition):
    bd = sqlite3.connect('data/bd.db')
    c = bd.cursor()
    if (not storyExists(title, c)):
        c.execute('CREATE TABLE "%s" (user TEXT, content TEXT)'%(title))
        c.execute('INSERT INTO "%s" VALUES ("%s", "%s")'%(title, user, addition))
        c.execute('INSERT INTO stories VALUES ("%s")'%(title))
        bd.commit()
        bd.close()
        
