from flask import Flask, render_template, request
from process import get_prediction
import pickle
import sklearn
from sklearn.linear_model import LinearRegression


app = Flask(__name__)

@app.route('/index', methods = ["get","post"])

def index():
  
    
  if request.method == "POST":
    with open('model_d.pkl', 'rb') as f:
      loaded_model = pickle.load(f)

    en = request.form.get('energy')
    
    co2 = loaded_model.predict([en])

    
    return render_template('index.html', result = co2)

    
