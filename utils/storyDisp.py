import sqlite3
from collections import OrderedDict

def getContent(story, c):
    content = []
    s = c.execute('SELECT * FROM %s'%(story))
    for r in s:
        content.append([r[1], r[0]])
    return content

def storyList():
    stories = OrderedDict()
    bd = sqlite3.connect('data/bd.db')
    c = bd.cursor()
    s = c.execute('SELECT * FROM stories')
    for r in s:
        story = r[0]
        content = getContent(story, c)
        stories[story] = content
    return stories
