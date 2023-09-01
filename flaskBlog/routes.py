from flask import render_template , url_for, flash, redirect
from flaskBlog import app
from flaskBlog.forms import RegistationForm , LoginForm
from flaskBlog.models import User , Post

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