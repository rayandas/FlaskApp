
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import os

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

posts = [
    {
        'author': 'Rayan Das',
        'title': 'Blog Post 1',
        'content': 'PyCon India 2019',
        'date_posted': 'Oct 20, 2019'
    },
    {
        'author': 'Sayan Chowdhury',
        'title': 'Blog Post 2',
        'content': 'Rootconf.In 2019',
        'date_posted': 'Aug 2, 2019'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)