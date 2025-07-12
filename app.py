import numpy as np
from flask import Flask, render_template, request
from process import get_prediction
import pickle
import sklearn 
from sklearn.linear_model import LinearRegression


app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])

def main():
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':
        with open('model.pkl', 'rb') as f:
            loaded_model = pickle.load(f)

        En = float(flask.request.form ['energy'])
        y_pred = loaded_model.predict([(En)])

        return render_template('index.html', result = y_pred)




    

 

  
