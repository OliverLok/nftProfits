import json
from urllib.parse import urlparse
import requests


def royaltyFees(collection):
    u = urlparse(collection)  # parses the url
    name = u.path  # gets the url path of what was inputed
    url = f"https://api.opensea.io/api/v1{name}"

    r = requests.get(url)  # requests data from the api

    packages_json = r.json()  # gets the json files from the requested api
    royalties_json = packages_json['collection'][
        'primary_asset_contracts']  # narrows down the data in the json file to a specific dictionary that contains the royalty fee (is a dictionary)

    packages_str = json.dumps(royalties_json)  # dumps json object into an element
    resp = json.loads(packages_str)  # load json into a string

    totalRoyalty = resp[0]['seller_fee_basis_points']  # gets the total royalty
    percentage = totalRoyalty / 10000
    return percentage
