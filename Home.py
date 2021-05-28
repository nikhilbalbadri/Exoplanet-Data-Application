import pandas as pd
import Data
from PlanetHottestStar import planetWithHottestStar
from GroupPlanet import groupPlanet
from OrphanPlanets import getOrphanPlanets
import config
from flask import Flask, render_template


app = Flask(__name__)

#Homepage
@app.route("/")
def home():
    return render_template('HomePage.html')

#Route to get number of orphan planets
@app.route('/orphanPlanets')
def orphanPlanets():
    numOrphanPlanets = getOrphanPlanets(data)
    return str(numOrphanPlanets)

#Route to get planet with Hottest star
@app.route('/hottestStarPlanet')
def hottestStarPlanet():
    planetName = planetWithHottestStar(data)
    return planetName

#Route to get Group by Planets based on Discovery Year and Size.
@app.route('/groupBySize')
def groupBySize():
    groupPlanets = groupPlanet(data)
    return groupPlanets


if __name__ == "__main__":
    url = config.URL
    data = pd.DataFrame(Data.loadData(url))
    app.run()


