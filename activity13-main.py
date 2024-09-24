from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('activity13.html', name="narender")


@app.route('/user/<name>')
def user(name):
    return render_template('activity13.html', name=name)

app.run(debug=True)