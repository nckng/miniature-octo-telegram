from flask import Flask, render_template, url_for, request, redirect, session
from utils import auth, homeDisp, storyCreate

app = Flask(__name__)
app.secret_key = 'nine'

@app.route('/')
@app.route('/login/')
def login():
    if 'user' in session:
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/home/')
def home():
    my = homeDisp.myStoryList(session['user'])
    non = homeDisp.nonStoryList(session['user'])
    myMsg = nonMsg = ""
    if (len(my) == 0):
        myMsg = "You haven't contributed to any stories :("
    if (len(non) == 0):
        nonMsg = "You've contributed to all the stories :)"
    return render_template('home.html', user = session['user'], myStories = my, nonStories = non, myMsg = myMsg, nonMsg = nonMsg)

@app.route('/write/')
def write():
    return render_template('write.html')

@app.route('/authenticate/', methods = ['POST'])
def authenticate():
    u = request.form['username']
    p = request.form['password']
    a = request.form['action']
    data = auth.authenticate([u, p, a])
    if data[1]:
        session['user'] = u
        return redirect(url_for('home'))
    else:
        return render_template('login.html', messageLogin = data[0])

@app.route('/create/', methods = ['POST'])
def create():
    title = request.form['title']
    text = request.form['addition']
    u = session['user']
    storyCreate.addStory (title, u, text)
    return redirect(url_for('home'))

@app.route('/logout/')
def logout():
    session.pop('user')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.debug = True
    app.run()
