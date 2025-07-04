from flask import Flask
from flask import render_template

app = Flask(name)

@app.route('/hello/<name>')
def hello(name):
  return render_template('hello.html', name=name)

if name == 'main':
  app.run(debug=True)
