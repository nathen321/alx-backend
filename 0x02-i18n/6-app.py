#!/usr/bin/env python3
'''Task 6: Force locale with URL parameter
'''

from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    '''Config class'''

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page.

    Returns:
        str: best match
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user:
        if g.user['locale'] in app.config["LANGUAGES"]:
            return g.user.get('locale')
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    '''default route

    Returns:
        html: homepage
    '''
    return render_template("6-index.html")


@app.before_request
def before_request():
    ''' user login system is outside the scope of this project.
    '''
    g.user = get_user()


def get_user():
    '''retreave user
    '''
    user = request.args.get('login_as')
    if user:
        return users.get(int(user))
    return None


if __name__ == '__main__':
    app.run()
