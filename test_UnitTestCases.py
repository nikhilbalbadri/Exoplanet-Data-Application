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

#Fixture function returning Data from URL in dataframe format to be used as input to test other functions
@pytest.fixture
def planetData():
    return Data.loadData(config.URL)

#Test case to verify if data contains required columns used in orphanPlanet function.
def test_orphanPlanetData(planetData):
    assert set(['HostStarMassSlrMass','HostStarRadiusSlrRad', 'HostStarAgeGyr','HostStarMetallicity', 'HostStarTempK', 'HostStarAgeGyr']).issubset(planetData.columns)

#Test to check if condition to extract orphan planets returns no data
def test_orphanPlanetNoData(planetData):
    data = OrphanPlanets.getOrphanPlanets(planetData)
    assert data != 0

#Test case to check if function orphanPlanets returns an integer value
def test_orphanPlanetReturnType(planetData):
    data = OrphanPlanets.getOrphanPlanets(planetData)
    assert type(data) == int

#Test case to check if function planetWithHottestStar returns a string
def test_planetWithHottestStarReturnType(planetData):
    data = PlanetHottestStar.planetWithHottestStar(planetData)
    assert type(data) == str

#Test case to verify if data contains required columns used in planetWithHottestStar function.
def test_planetWithHottestStarData(planetData):
    assert set(['HostStarTempK','PlanetIdentifier']).issubset(planetData.columns)

#Test case to check if function groupPlanet returns a string
def test_groupPlanetReturnType(planetData):
    data = GroupPlanet.groupPlanet(planetData)
    assert type(data) == str

#Test case to verify if data contains required columns used in groupPlanet function.
def test_groupPlanetData(planetData):
    assert set(['RadiusJpt','DiscoveryYear']).issubset(planetData.columns)

#Test case to verify if output of groupPlanet function is set in html table format
def test_groupPlanetResultData(planetData):
    data = GroupPlanet.groupPlanet(planetData)
    assert "table" in data

def test_groupPlanetResultData1(planetData):
    data = GroupPlanet.groupPlanet(planetData)
    assert "tbody" in data