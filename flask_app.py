'''
A flask application for controlled experiment on
the attention on advertisement with and
without clickbait healdines

Models stored in model.py

Flow of app:

1. Welcome Screen + some introduction on survey
2. Introduction to curiosity measure
3. Curiosty Measure
4. Introduction to attention measure
5. Attention Measure
6. Introduction to Study
7. Study

'''

# imports
from flask import Flask, render_template, url_for, redirect, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date, timedelta
import random , string
import json

# initializing the App and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///store.db'
db = SQLAlchemy(app)

# function for generation of random string
def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

# app route : root
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/sample')
def sample():
  return render_template('sample.html')

if __name__ == "__main__":
  app.run(debug=True)