from flask import Flask, escape, request
from flask import render_template

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


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')   

if __name__ == '__main__':
    app.run(debug=True)    