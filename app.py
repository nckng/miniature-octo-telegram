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
    if 'user' in session:
        s = storyDisp.storyList()
        return render_template('home.html', messageHome = session['user'], stories = s)
    else:
        return redirect(url_for('login'))

@app.route("/authenticate/", methods=['POST'])
def authenticate():
    u = request.form['username']
    p = request.form['password']
    a = request.form['action']
    if (a == 'Register'):
        msg = auth.register(u, p)
        return render_template('login.html', messageLogin = msg)
    else:
        msg = auth.login(u, p)
        if (msg == 'Login successful.'):
            session['user'] = u
            return redirect(url_for('home'))
        else:
            return render_template('login.html', messageLogin = msg)

@app.route("/logout/")
def logout():
    session.pop('user')
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.debug = True
    app.run()
