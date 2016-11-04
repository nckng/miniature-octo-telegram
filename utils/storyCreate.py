import sqlite3

def storyExists(title, c):
    s = c.execute('SELECT name FROM stories')
    for r in s:
        name = r[0]
        if story == name:
            return True;
    return False;

def addStory(title, user, text):
    result = []
    bd = sqlite3.connect('data/bd.db')
    c = bd.cursor()
    if (storyExists(title, c)):
        result = ['Story already exists.', False]
    elif len(title) == 0 or len(text) == 0:
         result = ['Missing title/text.', False]
    else:
        c.execute('CREATE TABLE %s (name TEXT, content TEXT)'%(title))
        c.execute('INSERT INTO %s VALUES ("%s", "%s")'%(title, user, text))
        bd.commit()
        bd.close()
        result = ['Creation successful.', False]
    return result
