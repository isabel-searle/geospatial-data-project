import os
from dotenv import load_dotenv
import json, requests
load_dotenv()
fs_token = os.getenv("foursquare_KEY")
fs_id = os.getenv("foursquare_ID")


def query_foursquare_explore(query,place):
    fs_id = os.getenv('foursquare_ID')
    fs_token = os.getenv('foursquare_KEY')
    url = 'https://api.foursquare.com/v2/venues/explore'
    params = dict(
    client_id=fs_id,
    client_secret=fs_token,
    near=place,
    query=query,
    limit=50,
    v='20201115'
    )
    resp = requests.get(url=url, params=params)
    return json.loads(resp.text)

def query_foursquare_search(query,place):
    fs_id = os.getenv('foursquare_ID')
    fs_token = os.getenv('foursquare_KEY')
    url = 'https://api.foursquare.com/v2/venues/search'
    params = dict(
    client_id=fs_id,
    client_secret=fs_token,
    near=place,
    query=query,
    limit=50,
    v='20201115'
    )
    resp = requests.get(url=url, params=params)
    return json.loads(resp.text)