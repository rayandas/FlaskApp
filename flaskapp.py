'''
from flask import Flask
from flask import render_template, url_for

app = Flask(__name__)


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
'''
from flask import Flask, render_template, url_for
app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)