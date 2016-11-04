import sqlite3

def storyExists(title, c):
    s = c.execute('SELECT name FROM stories')
    for r in s:
        name = r[0]
        if title == name:
            return True;
    return False;

def addStory(title, user, text):
    bd = sqlite3.connect('data/bd.db')
    c = bd.cursor()
    if (storyExists(title, c)):
        return 'Story already exists.'
    elif len(title) == 0 or len(text) == 0:
         return 'Missing title/text.'
    else:
        c.execute('CREATE TABLE %s (name TEXT, content TEXT)'%(title))
        c.execute('INSERT INTO %s VALUES ("%s", "%s")'%(title, user, text))
        bd.commit()
        bd.close()
        return 'Creation successful.'
