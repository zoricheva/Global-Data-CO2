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
    energy = request.form.get("energy")
    try:
        energy = float(energy)
    except Exception as e:
      print(e)
      message += "Некорректный ввод. Установлено значение по умолчанию: 0 "
      energy = 0.0

    co2 = get_prediction(energy)

    #with open('model_ex.pkl','rb') as f:
    #loaded_model = pickle.load(f)

      #model = pickle.load(open('model_ex.pkl','rb'))
      #co2 = model.predict([[energy]])

    message = f"При потребляемой энергии в размере {energy} количество выбросов будет равно {co2} "
    
  
  return render_template("index2.html", message = message)


  
 # if request.method == "GET": 
  #  return render_template('index.html')
    
  #if request.method == "POST":
    #en = request.form.get('energy')
    
   # with open('model_d.pkl','rb') as f:
    #  loaded_model = pickle.load(f)

   # co2 = loaded_model.predict(en)

    
    #energy = request.form.get("energy")
    #co2 = get_prediction(energy)

    
   # return render_template('index.html', result = co2)

    
