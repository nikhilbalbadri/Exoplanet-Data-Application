#Calculate number of Orphan planets
def getOrphanPlanets(data):
    numOrphanPlanets = data[(data['HostStarMassSlrMass'] == '') & (data['HostStarRadiusSlrRad'] == '') & (data['HostStarAgeGyr'] == '') & (data['HostStarMetallicity'] == '') & (data['HostStarTempK'] == '') & (data['HostStarAgeGyr'] == '')].shape[0]
    return numOrphanPlanets
