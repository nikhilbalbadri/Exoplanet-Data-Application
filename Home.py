import pandas as pd
import Data
from PlanetHottestStar import planetWithHottestStar
from GroupPlanet import groupPlanet
from OrphanPlanets import getOrphanPlanets
import config
from flask import Flask, render_template


app = Flask(__name__)
url = config.URL
data = pd.DataFrame(Data.loadData(url))
@app.route("/")
def home():
    return render_template('HomePage.html')

@app.route('/orphanPlanets')
def orphanPlanets():
    numOrphanPlanets = getOrphanPlanets(data)
    return render_template('HomePage.html', orphanPlanets = '{}'.format(numOrphanPlanets))
@app.route('/hottestStarPlanet')
def hottestStarPlanet():
    planetName = planetWithHottestStar(data)
    return render_template('HomePage.html', hottestStarPlanetName = '{}'.format(planetName))

@app.route('/groupBySize')
def groupBySize():
    result = groupPlanet(data)
    return render_template('HomePage.html', groupPlanets = result)


if __name__ == "__main__":
    app.run()


