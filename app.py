from flask import Flask, render_template, url_for, request, redirect, session
from utils import auth

app = Flask(__name__)
app.secret_key = "nine"


@app.route("/")
def home():
    print request
    if ('user' in session.keys() and auth.userExists(session['user'])):
        mHome = "Welcome back " + session['user'] + "!"
        return render_template('home.html', messageHome=mHome)
    else:
        return redirect(url_for('login'))


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/authenticate", methods=['POST'])
def authenticate():
    u = request.form['username']
    p = request.form['password']
    a = request.form['action']
    if (a == 'Login' or a == 'Register'):
        return auth.task(u, p, a)
    else:
        return redirect(url_for('login'))


@app.route("/logout", methods=['POST'])
def logout():
    session.pop('user')
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.debug = True
    app.run()
