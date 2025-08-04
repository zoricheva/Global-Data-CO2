from flask import Flask, render_template, request
from process import get_prediction

app = Flask(__name__)

@app.route('/hello')
def hello():

  return render_template("index.html")
