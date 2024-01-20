from flask import Flask,render_template
import json
app = Flask(__name__)

from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/')
def index():
    return json.dumps({'name':'name'})

@app.route('/user/<name>')
def index1(name):
    fruits = ['apple','orange']
    return render_template('user.html',name=name,fruits=fruits)

if __name__ == '__main__':
    app.run(debug=True) #debug reloads application after changes and show error detailly