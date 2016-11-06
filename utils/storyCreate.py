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
    if (not (storyExists(title, c) or len(title) == 0 or len(addition) == 0)):
        c.execute('CREATE TABLE %s (user TEXT, addition TEXT);' %(title))
        c.execute('INSERT INTO %s (user, addition) VALUES ("%s", "%s");' %(title, user, addition))
        c.execute('INSERT INTO stories (name) VALUES ("%s");' %(title))
        bd.commit()
        bd.close()
