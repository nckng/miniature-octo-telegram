from flask import Flask, render_template, url_for, request, redirect, session
from utils import auth, storyDisp

app = Flask(__name__)
app.secret_key = "nine"

@app.route("/")
@app.route("/login/")
def login():
    if 'user' in session:
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route("/home/")
def home():
        s = storyDisp.storyList()
        return render_template('home.html', messageHome = session['user'], stories = s)

@app.route("/authenticate/", methods = ['POST'])
def authenticate():
    data = [request.form['username'], request.form['password'], request.form['action']]
    data = auth.authenticate(data)
    if data [1]:
        session ['user'] = True
        return redirect(url_for('home'))
    else:
        return render_template('login.html', messageLogin = data [0])

@app.route("/logout/")
def logout():
    session.pop('user')
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.debug = True
    app.run()
