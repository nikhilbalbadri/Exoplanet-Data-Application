def planetWithHottestStar(data):
    data = data.replace('',0)
    maxTemp = data['HostStarTempK'].max()
    planetName = data[data['HostStarTempK'] == maxTemp].PlanetIdentifier.item()
    return planetName