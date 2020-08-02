from os import environ
from flask import Flask, render_template
import main as twitter

app = Flask(__name__)


@app.route("/bot")
def home():
    twitter.main()


@app.route('/')
def root():
    return render_template('index.html')


app.run(debug=True)
