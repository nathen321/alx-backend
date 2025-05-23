#!/usr/bin/env python3
'''Task 2: Basic Flask app
'''

from flask import Flask, render_template
from flask_babel import Babel
from flask import request

app = Flask(__name__)


class Config:
    '''configuration class'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    '''default route'''
    return render_template('2-index.html')


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page.

    Returns:
        str: best match
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
