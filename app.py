from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': "au au",
        'title': "titi",
        'content': 'sample contenct smaple content',
        'date_posted': 'April 21, 2020',
    },
    {
        'author': "auttretet au",
        'title': "tetreteiti",
        'content': 'sample cotwtwrtetntenct smaple content',
        'date_posted': 'April 21, 2020',
    },
    {
        'author': "aufdsf au",
        'title': "tifdsfti",
        'content': 'sample contenct sfdsfsmaple content',
        'date_posted': 'April 21, 2020',
    },
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run()
