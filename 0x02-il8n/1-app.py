#!/usr/bin/env python3
"""
 initialization of the Flask-Babel extension
"""
from flask import request, Flask, render_template

from flask_babel import Babel


class Config(object):
    """config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TZ = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def hello_world():
    """ Greeting

        Return:
            Initial template html
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
