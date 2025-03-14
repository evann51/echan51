from flask import Flask, render_template, redirect, url_for, request, session
from datetime import datetime
from jinja2 import Template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Simulated in-memory database
users = {}
posts = []

@app.context_processor
def inject_user():
    current_user = {'is_authenticated': 'username' in session, 'username': session.get('username')}
    return dict(current_user=current_user)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and user['password'] == password:
            session['username'] = username
            return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        content = request.form['content']
        post = {
            'content': content,
            'author': session['username'],
            'timestamp': datetime.utcnow()
        }
        posts.append(post)
        return redirect(url_for('home'))
    return render_template('create_post.html')

@app.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    if 'username' not in session:
        return redirect(url_for('login'))
    post = posts[post_id]
    if post['author'] != session['username']:
        return redirect(url_for('home'))
    if request.method == 'POST':
        post['content'] = request.form['content']
        post['timestamp'] = datetime.utcnow()
        return redirect(url_for('home'))
    return render_template('edit_post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
