import Data
import config
import GroupPlanet
import OrphanPlanets
import PlanetHottestStar
import re
import pytest

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


#Test case to validate url stored
def test_ValidURL():
    assert re.match(regex,config.URL)

#Test case to validate if empty URL
def test_emptyURL():
    assert config.URL

#Test case to check if url has no data and returned Dataframe is empty
def test_loadData():
    data = Data.loadData(config.URL)
    assert not data.empty

@pytest.fixture
def planetData():
    return Data.loadData(config.URL)

def test_orphanPlanet(planetData):
    data = OrphanPlanets.getOrphanPlanets(planetData)
    assert type(data) == int
    assert data

def test_planetWithHottestStar(planetData):
    data = PlanetHottestStar.planetWithHottestStar(planetData)
    assert type(data) == str
    assert data

def test_planetWithHottestStarString(planetData):
    data = PlanetHottestStar.planetWithHottestStar(planetData)
    assert type(data) == str

def test_groupPlanet(planetData):
    data = GroupPlanet.groupPlanet(planetData)
    assert data