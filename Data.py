import pandas as pd

#Read data from URL
def loadData(url):
    data = pd.DataFrame()
    data = pd.read_json(url)
    return data
