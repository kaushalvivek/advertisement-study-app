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

@app.route('/mode')
def mode():
  return render_template('mode.html')

@app.route('/control')
def control():
  mode = request.args.get('mode')
  if mode == 1:
    headlines = headlines_clickbait
  else:
    headlines = headlines_non_clickbait
  
  return render_template('mode.html')

@app.route('/apple')
def apple():
  return render_template('apple.html')

@app.route('/delhi')
def delhi():
  return render_template('delhi.html')  

@app.route('/justice')
def justice():
  return render_template('justice.html')

@app.route('/train')
def train():
  return render_template('train.html')

@app.route('/volcano')
def volcano():
  return render_template('volcano.html')

@app.route('/law')
def law():
  return render_template('law.html')

if __name__ == "__main__":
  app.run(debug=True)