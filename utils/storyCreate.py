import sqlite3

def storyExists(title, c):
    s = c.execute('SELECT name FROM stories')
    for r in s:
        name = r[0]
        if title == name:
            return True
    return False

def addStory(title, user, content):
    result = []
    bd = sqlite3.connect('data/bd.db')
    c = bd.cursor()
    if storyExists(title, c):
        result = ['A story with that title already exists.', False]
    elif len(title) == 0:
        result = ['Your story needs a title.', False]
    elif len(content) == 0:
        result = ['Your story needs content.', False]
    else:
        c.execute('CREATE TABLE "%s" (user TEXT, content TEXT)'%(title))
        c.execute('INSERT INTO "%s" VALUES ("%s", "%s")'%(title, user, content))
        c.execute('INSERT INTO stories VALUES ("%s")'%(title))
        bd.commit()
        bd.close()
        result = ['', True]
    return result
