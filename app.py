from flask import Flask, render_template, request
from process import get_prediction
import pickle
import sklearn
from sklearn.linear_model import LinearRegression


app = Flask(__name__)

@app.route('/', methods = ["get","post"])

def hello():
  
  if request.method == "GET": 
    return render_template('index.html')
    
  if request.method == "POST":
    #en = request.form.get('energy')
    en = 5
    with open('model_d.pkl','rb') as f:
      loaded_model = pickle.load(f)

   
    co2 = loaded_model.predict(en)

    
    return render_template('index.html', result = co2)

    
