from flask import Flask, render_template, request
from process import get_prediction
from sklearn.preprocessing import MinMaxScaler
import pickle
import sklearn



app = Flask(__name__)

@app.route('/', methods = ["get","post"])

def hello():
  message = ""
  if request.method == "POST":
    energy1 = request.form.get("energy1")
    energy2 = request.form.get("energy2")
    energy3 = request.form.get("energy3")
    try:
        energy1 = float(energy1)
        energy2 = float(energy2)
        energy3 = float(energy3)
    except Exception as e:
      print(e)
      message += "Некорректный ввод. Установлено значение по умолчанию: 0 "
      energy = 0.0

    en = [energy1, energy2, energy3]
    
    minmax_scaler = MinMaxScaler()
    e = minmax_scaler.fit_transform(en)
    energy = minmax_scaler.transform(np.array(e))

    co2 = get_prediction(energy)


    message = f"Количество выбросов углекислого газа: {co2} "
    
  
  return render_template("index.html", message = message)


  
 # if request.method == "GET": 
  #  return render_template('index.html')
 

    
   # return render_template('index.html', result = co2)

    
