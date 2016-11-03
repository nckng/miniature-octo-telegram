"from flask import render_template, url_for, request, redirect, session"
import hashlib, sqlite3

def hashPass(password):
    return hashlib.sha512(password).hexdigest()

def userExists(username, c):
    s = c.execute('SELECT name FROM users')
    for r in s:
        name = r[0]
        if username == name:
            return True;
    return False;

def register(user, password):
    bd = sqlite3.connect('data/bd.db')
    c = bd.cursor()
    if (userExists(user, c)):
        return 'User already exists.'
    elif len(user) == 0 or len(password) == 0:
        return 'Invalid username/password.'
    else:
        p = hashPass(password)
        c.execute('INSERT INTO users VALUES (\'' + user + '\', \'' + p + '\');')
        bd.commit()
        bd.close()
        return 'Registration successful.'

def login(user, password):
    bd = sqlite3.connect('data/bd.db')
    c = bd.cursor()
    if (userExists(user, c) == False):
        return 'User does not exist.'
    else:
        s = c.execute('SELECT password FROM users WHERE name = \'' + user + '\';')
        p = s.fetchone()[0]
        if (p != hashPass(password)):
            return 'Incorrect password.'
        else:
            return 'Login successful.'
