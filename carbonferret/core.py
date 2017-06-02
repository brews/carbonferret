import requests
import pandas


def find_near(lat, lon, *, n=10, session=None):
    """Return n results for a given latitude and longitude"""
    search_params = {'npoints': n, 'clat': lat, 'clon': lon, 
                     'Columns[]': ['Subregion', 'Notes', 'CollectionYear', 
                                   'ReservoirAge', 'ReservoirErr', 'C14age', 
                                   'C14err', 'LabID', 'Delta13C', 'nextime', 
                                   'Genus', 'Species', 'Feeding', 'Name']}
    resp = _query_near(session=session, **search_params)
    df = _response_to_dataframe(resp)
    df_clean = _clean_dataframe(df)
    return df_clean


def _query_near(*, session=None, **kwargs):
    """Query marine database with given query string values and keys"""
    url_endpoint = 'http://calib.org/marine/index.html'
    if session is not None:
        resp = session.get(url_endpoint, params=kwargs)
    else:
        with requests.Session() as s:
            # Need to get the index page before query. Otherwise get bad query response that seems legit.
            s.get('http://calib.org/marine/index.html')
            resp = s.get(url_endpoint, params=kwargs)
    return resp


def _response_to_dataframe(x):
    """Convert tables in HTML response, x, to list of pandas dataframes"""
    df = pandas.read_html(x.text, header=0)
    return df


def _clean_dataframe(df):
    """Clean response list of pandas dataframes to query results table"""
    cleaned = df[3]
    del cleaned['Unnamed: 0']
    del cleaned['Unnamed: 23']
    return cleaned
