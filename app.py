from flask import Flask, render_template, request
from process import get_prediction
from sklearn.preprocessing import MinMaxScaler
import pickle
import sklearn

app = Flask(__name__)

@app.route('/', methods = ["get","post"])

def hello():



  return render_template("index.html", message = message)
