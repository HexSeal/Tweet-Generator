from flask import Flask
import sample

app = Flask(__name__)

@app.route('/')
def harry_potter_sample():
    return sample.word_sampler("hpb1_hist.txt")