from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def index1(name):
    return render_template('user.html',name=name)

if __name__ == '__main__':
    app.run(debug=True) #debug reloads application after changes and show error detailly