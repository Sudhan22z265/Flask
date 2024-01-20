from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>hello</h1>'

@app.route('/user/<name>')
def index1(name):
    return f'<h1>hello{name}</h1>'

if __name__ == '__main__':
    app.run(debug=True) #debug reloads application after changes and show error detailly