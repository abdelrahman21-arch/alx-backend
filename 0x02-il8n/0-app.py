#!/usr/bin/env python3
"""
first flask app
"""

from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    """ Greeting

           Return:
               Initial template html
       """
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(debug=True)


