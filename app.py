from flask import Flask, render_template, request, redirect, url_for

from dictogram import Dictogram
import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Tweet-Generator')

app = Flask(__name__)

@app.route('/')
def index():
    """ Homepage """
    word_doc = 'harry_potterb1.txt'
    words = run(word_doc)
    histogram = Dictogram(words)
    sentence = histogram.get_sentence(15)
    return render_template("index.html", tweet=sentence)

if __name__ == "__main__":
    app.run(Debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))