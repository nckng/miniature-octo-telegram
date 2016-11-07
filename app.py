from flask import Flask, render_template, url_for, request, redirect, session
from utils import auth, homeDisp, storyCreate, storyDisp

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
    if 'user' in session:
        my = homeDisp.myStoryList(session['user'])
        non = homeDisp.nonStoryList(session['user'])
        myMsg = nonMsg = ""
        if (len(my) == 0):
            myMsg = "You haven't contributed to any stories :("
        if (len(non) == 0):
            nonMsg = "You've contributed to all the stories :)"
        return render_template('home.html', user = session['user'], myStories = my, nonStories = non, myMsg = myMsg, nonMsg = nonMsg)
    else:
        return redirect(url_for('login'))

@app.route('/write/')
def write():
    if 'user' in session:
        return render_template('write.html')
    else:
        return redirect(url_for('login'))

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
    text = request.form['content']
    u = session['user']
    data = storyCreate.addStory(title, u ,text)
    if data[1]:
        return redirect(url_for('home'))
    else:
        return render_template('write.html', messageCreate = data[0])

@app.route('/renderStory/', methods = ['POST'])
def renderStory():
    storyTitle = request.form['title']
    storyAuthor = storyDisp.genAuthor(storyTitle)
    if storyDisp.hasContributed(session['user'], storyTitle):
        storyDict = storyDisp.genStory(storyTitle)
        return render_template('view.html', story = storyDict, title = storyTitle, author = storyAuthor)
    if not storyDisp.hasContributed(session['user'], storyTitle):
        lastLine = storyDisp.genLast(storyTitle)
        return render_template('comment.html', last = lastLine, title = storyTitle, author = storyAuthor)

@app.route('/addComment/', methods = ['POST'])
def addComment():
    storyTitle = request.form['title']
    storyText = request.form['comment']
    user = session['user']
    storyCreate.addComment(user, storyTitle, storyText)
    storyDict = storyDisp.genStory(storyTitle)
    storyAuthor = storyDisp.genAuthor(storyTitle)
    return redirect(url_for('renderStory'), code = 307)

@app.route('/logout/')
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.debug = True
    app.run()
