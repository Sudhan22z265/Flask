from flask import Flask,render_template
import json
app = Flask(__name__)

from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return json.dumps({'name':'name'})

@app.route('/user/<name>')
def index1(name):
    fruits = ['apple','orange']
    return render_template('user.html',name=name,fruits=fruits)

if __name__ == '__main__':
    app.run(debug=True) #debug reloads application after changes and show error detailly