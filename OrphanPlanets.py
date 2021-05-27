
def getOrphanPlanets(data):
    numOrphanPlanets = data[(data['HostStarMassSlrMass'] == '') & (data['HostStarRadiusSlrRad'] == '') & (data['HostStarAgeGyr'] == '')].shape[0]
    return numOrphanPlanets
