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
    energy = request.form.get('energy')
    try:
      energy = float(energy)
    except Exception as e:
      print(e)
      message += "Некорректный ввод. Установленно значение по умолчанию:0"
      
      with open('model.pkl', 'rb') as f:
        loaded_model = pickle.load(f)
    y_pred = loaded_model.predict([(energy)])
    message = f"Предскаание {energy} равна {y_pred} рублей"
    
  return render_template('index.html', message=message)




    

 

  
