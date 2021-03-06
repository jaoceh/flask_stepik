from flask import Flask, render_template
import data
from random import randint

app = Flask(__name__)



@app.route('/')
def main():
    pinned_tours = {}
    while len(pinned_tours) < 6:
        id = randint(1,16)
        pinned_tours[id] = data.tours[id]
    return render_template('index.html', subtitle=data.subtitle, title=data.title, description=data.description, pinned_tours=pinned_tours, departures=data.departures)

@app.route('/departures/<departure>')
def departure(departure):
    departure_tours = {}
    departure_tour_prices = []
    departure_tour_nights = []
    for k, v in data.tours.items():
        if v['departure'] == departure:
            departure_tours[k]=v
            departure_tour_prices.append(v['price'])
            departure_tour_nights.append(v['nights'])
    return render_template('departure.html', title=data.title, departure_tours = departure_tours, departures=data.departures, departure_tour_prices=departure_tour_prices, departure_tour_nights=departure_tour_nights)

@app.route('/tours/<id>')
def tour(id):
    id = int(id)
    tour = data.tours[id]
    departure = data.departures[tour['departure']]
    return render_template('tour.html', tour=tour, departure=departure, title=data.title, departures=data.departures)


if __name__ == '__main__':
    app.run(debug=True)

