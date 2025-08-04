
from flask import Flask, render_template, request
from process import get_prediction
import pickle
 


app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def hello():
  message = ''
  if request.method == 'POST':
    energy = flask.request.form ['energy']
      
    co2 = get_prediction(energy)
    message = f"Предсказание:{co2}"
  return render_template('index.html', message = message)





