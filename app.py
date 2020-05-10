from flask import Flask, render_template    # сперва подключим модуль
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)      # объявим экземпляр фласка

app.debug = True

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = '183-618-819'

toolbar = DebugToolbarExtension(app)

@app.route('/')
def main():
    return render_template('bootstrap.html')

@app.route('/departures/<departure>')
def departure(departure):
    return render_template('departure.html')

@app.route('/tours/<id>')
def tour(id):
    return render_template('tour.html')



app.run('0.0.0.0',8000, debug=True)    # запустим сервер на 8000 порту!
