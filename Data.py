import pandas as pd

def loadData(url):
    data = pd.DataFrame()
    data = pd.read_json(url)
    return data