#Group planet by discovery year and Size
def groupPlanet(data):
    data = data[data['RadiusJpt']!='']
    data = data.assign(Size='') #Creating new column 'SIZE'
    data.loc[data['RadiusJpt'] > 2.0, 'Size'] = 'large'
    data.loc[data['RadiusJpt'] < 2.0, 'Size'] = 'medium'
    data.loc[data['RadiusJpt'] < 1.0, 'Size'] = 'small'
     #Grouping planet by discovery year and Size and converting it to html table format(in string)
    result = data.groupby(['DiscoveryYear','Size']).size().to_frame('Number of Planets Discovered').to_html()
    return result
