import numpy as np
from flask import Flask, render_template, request
from process import get_prediction
import pickle
import sklearn 
from sklearn.linear_model import LinearRegression



app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def hello():
  message = ''
  if request.method == 'POST':
    try:
      En = float(flask.request.form ['energy'])
         
      with open('model.pkl', 'rb') as f:
        loaded_model = pickle.load(f)
    except Exception as e:
        print(e)
        message += f"Некорректный ввод. Установленно значение по умолчанию:0"
        En = 0.0
    y_pred = loaded_model.predict([(En)])
    message += f"Предсказание:{y_pred}"
  return render_template('index.html', result = message)




    

 

  
