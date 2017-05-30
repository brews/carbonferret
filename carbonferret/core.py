import requests
import pandas


def find_near(lat, lon, *, n=10):
    search_params = {'npoints': n, 'clat': lat, 'clon': lon, 
                     'Columns[]': ['Subregion', 'Notes', 'CollectionYear', 
                                   'ReservoirAge', 'ReservoirErr', 'C14age', 
                                   'C14err', 'LabID', 'Delta13C', 'nextime', 
                                   'Genus', 'Species', 'Feeding', 'Name']}
    resp = _query_near(**search_params)
    df = _resp_to_dataframe(resp)
    df_clean = _clean_dataframe(df)
    return df_clean


def _query_near(**kwargs):
    url_endpoint = 'http://calib.org/marine/index.html'
    resp = None
    with requests.Session() as s:
        s.get('http://calib.org/marine/index.html')
        resp = s.get(url_endpoint, params=kwargs)
    return resp


def _resp_to_dataframe(x):
    df = pandas.read_html(x.text, header=0)
    return df


def _clean_dataframe(d):
    cleaned = d[3]
    del cleaned['Unnamed: 0']
    del cleaned['Unnamed: 23']
    return cleaned
