from datetime import datetime
from flask import Flask, render_template , url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistationForm , LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False, unique = True)
    email = db.Column(db.String(120), nullable = False, unique = True)
    image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')
    password = db.Column(db.String(60), nullable = False)
    post = db.relationship('Post', backref='author', lazy = True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}, '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted})"

posts = [
    {
        'author'  : 'K V D Sridhar',
        'title'   : 'Blog post 1',
        'content' : 'this is the first blog post',
        'data_posted' : '29 August 2023'

    },

    {
        'author'  : 'Erling Haaland',
        'title'   : 'Blog post 2',
        'content' : 'this is the second blog post',
        'data_posted' : '30 August 2023'

    },

]

# two different decorators(routes) pointing towards a single page.
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

# adding extra routes.
@app.route("/about")
def about():
    return render_template('about.html', title = 'about')

@app.route("/register", methods = ['GET','POST'])
def register():
    form = RegistationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}", 'success')
        return redirect(url_for('home'))
    
    return render_template('register.html', title = 'register', form = form)

@app.route("/login",methods = ['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login',form = form)

# This condition is used to run the flask server directly using app.py file.
if __name__ == '__main__':
    app.run(debug=True)

