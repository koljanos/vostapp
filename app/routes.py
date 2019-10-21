from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Васян'}
    posts = [
        {
            'author': {'username': 'Тимофей'},
            'body': 'А можно я с вами свалю с иностранного языка?'
        },
        {
            'author': {'username': 'Николай'},
            'body': 'Нет, низзя!'
        },
        {
            'author': {'username': 'Николай'},
            'body': 'БУБУБУ!'
        },
        {
            'author': {'username': 'Николай'},
            'body': 'БАБАБА'
        },
        {
            'author': {'username': 'Николай'},
            'body': 'ЯЯЯ'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
