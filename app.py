from flask import Flask, render_template, request
from process import get_prediction
from sklearn.preprocessing import MinMaxScaler
import pickle
import sklearn

app = Flask(__name__)

@app.route('/', methods = ["get","post"])

def hello():
  if request.method == "POST":
    energy1 = request.form.get("energy1")
    energy2 = request.form.get("energy2")
    energy3 = request.form.get("energy3")
    try:
        energy1 = float(energy1)
        energy2 = float(energy2)
        energy3 = float(energy3)



  return render_template("index.html", message = message)
