from flask import render_template, url_for, request, redirect, session
import hashlib, sqlite3, csv

def scanDB():
    bd = sqlite3.connect('bd.db')
    c = bd.cursor()
    return 

def appendCSV(file, string):
    outstream = open(file, 'a')
    outstream.write(string)
    outstream.close()


def genList(string):
    L1 = string.split("\n")
    L2 = []
    for a in L1:
        a = a.split(",")
        L2 += [a]
    return L2

def userExists(username):
    c = scanDB()
    s = c.execute('SELECT name FROM users')
    for name in s:
        if username == name:
            return True;
    return False;

def hashPass(password):
    return hashlib.md5(password).hexdigest()


def task(username, password, action):
    userList = genList(scanCSV('data/users.csv'))
    if action == 'Login':
        for account in userList:
            if (username == account[0] and hashPass(password) == account[1]):
                session['user'] = username
                return redirect(url_for('home'))
            if (username == account[0] and not hashPass(password) == account[1]):
                m = "Incorrect password."
                return render_template("login.html", messageLogin=m)
        m = "Username does not exist."
        return render_template("login.html", messageLogin=m)
    else:
        exists = False
        for account in userList:
            if username == account[0]:
                exists = True
        if exists:
            m = "The username already exists."
            return render_template("login.html", messageLogin=m)
        else:
            newUser = username + "," + hashPass(password) + "\n"
            appendCSV('data/users.csv', newUser)
            m = "Account successfully created."
            return render_template("login.html", messageLogin=m)
