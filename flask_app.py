'''
A flask application for controlled experiment on
the attention on advertisement with and
without clickbait healdines
'''

# imports
from flask import Flask, render_template, url_for, redirect, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date, timedelta
import random , string
import json

# initializing the App and database
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///store.db'
# db = SQLAlchemy(app)

# function for generation of random string
def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


cb_headlines = {
  'apple':"You won't believe what Apple is planning for India!",
  'delhi':"You won't believe how Delhi is tackling open defecation!!",
  'justice':"Justice delivered",
  'train':"If this woman isn't the luckiest person alive, then we don't know who is",
  'volcano':"Volcanoes in India?! This is what top scientists have to say",
  'law':"That's the running joke among Indian entrepreneurs"
}

ncb_headlines = {
  'apple':"Apple wants to start making iPhones in India",
  'delhi':"Delhi mascots to blow the whistle on public defecation",
  'justice':"Hyderabad Blasts Case: Yasin Bhatkal sentenced to death",
  'train':"Woman evades approaching train by lying on tracks",
  'volcano':"The Barren Island volcano, India's only live volcano, is active again",
  'law':"Indian laws make it easier to start a company than to shut one down"
}

sequence = 1
headlines = {}

links = ['apple','delhi','justice','train','volcano','law']

# app route : root
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/mode')
def mode():
  return render_template('mode.html')

@app.route('/mode_control')
def mode_control():
  print('here')
  global headlines
  global links
  mode = int(request.args.get('mode'))
  if mode % 2 == 1:
    headlines = cb_headlines
    random.shuffle(links)
  else:
    headlines = ncb_headlines
    random.shuffle(links)
  return redirect('/'+links[sequence-1])
  
@app.route('/control')
def control():
  global sequence
  global headlines
  global links
  sequence +=1
  if sequence <= 6:
    return redirect('/'+links[sequence-1])
  else:
    return render_template('end.html')

@app.route('/apple')
def apple():
  return render_template('apple.html',title=headlines['apple'])

@app.route('/delhi')
def delhi():
  return render_template('delhi.html', title=headlines['delhi'])

@app.route('/justice')
def justice():
  return render_template('justice.html', title=headlines['justice'])

@app.route('/train')
def train():
  return render_template('train.html', title=headlines['train'])

@app.route('/volcano')
def volcano():
  return render_template('volcano.html', title=headlines['volcano'])

@app.route('/law')
def law():
  return render_template('law.html', title=headlines['law'])

@app.route('/end')
def end():
  return render_template('end.html')

if __name__ == "__main__":
  app.run(debug=True)