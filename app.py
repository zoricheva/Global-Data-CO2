from flask import Flask, render_template, request
from process import get_prediction
import pickle
import sklearn
from sklearn.linear_model import LinearRegression


app = Flask(__name__, template_folder = 'templates')

@app.route('/', methods=["get", "post"])
@app.route('/index', methods=["get", "post"])

def index():
  message = ""
  if request.method == "GET":
    return render_template('index.html')
    
  if request.method == "POST":
    with open('model_d.pkl', 'rb') as f:
      loaded_model = pickle.load(f)

    en = float(request.form['energy'])
    co2 = loaded_model.predict([[en]])

    message = f"При потребляемой энергии в размере {en} количество выбросов будет равно {co2} " 
    return render_template('index.html', message = message)

    
