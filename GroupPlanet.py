def groupPlanet(data):
    data = data[data['RadiusJpt']!='']
    data = data.assign(Size='')
    data.loc[data['RadiusJpt'] > 2.0, 'Size'] = 'large'
    data.loc[data['RadiusJpt'] < 2.0, 'Size'] = 'medium'
    data.loc[data['RadiusJpt'] < 1.0, 'Size'] = 'small'
    result = data.groupby(['DiscoveryYear','Size'])['PlanetIdentifier'].agg(['count']).apply(list).to_dict()['count']
    return result