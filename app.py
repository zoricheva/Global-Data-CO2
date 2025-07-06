from flask import Flask, render_template, request
from process import get_prediction

app = Flask(__name__)

@app.route('/', methods = ['post','get'])
def hello():
  message = ''
  if request.method == 'POST':
    area = request.form.get('area')
    try:
      area = float(area)
    except Exception as e:
      print(e)
      message += "Некорректный ввод. Установленно значение по умолчанию:0"
    cost = get_prediction(area)
    message = f"Стоимость квартиры площадью {area} равна {cost} рублей"
  return render_template('index.html', message=message)

  
