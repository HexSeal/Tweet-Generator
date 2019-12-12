from flask import Flask, render_template, request, redirect, url_for
from higher_order_markov import SecondOrderChain

import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Tweet-Generator')

app = Flask(__name__)

@app.route('/')
def index():
    """ Homepage """
    word_list = SecondOrderChain.get_text("jordanpeterson.txt")
    markov_chain = SecondOrderChain(word_list)
    sentence = markov_chain.word_walk(8)

    return render_template("index.html", tweet=sentence)

if __name__ == "__main__":
    app.run(Debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))