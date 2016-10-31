from flask import render_template, url_for, request, redirect, session
import hashlib


def scanCSV(file):
    instream = open(file, 'r')
    content = instream.read().strip()
    instream.close()
    return content


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
    userList = genList(scanCSV('data/users.csv'))
    ans = False
    for account in userList:
        if username == account[0]:
            ans = True
    return ans


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
