import requests
import utils
import json
from flask import jsonify

def get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.request("GET", url)
    return response.json()


 
def get_albums():
    url = "https://jsonplaceholder.typicode.com/albums"
    response = requests.request("GET", url)
    return response.json()


def get_user_albums(userid):
    if(utils.checkInputFormat(userid)):
        querystring = {"userId":userid}
        url = "https://jsonplaceholder.typicode.com/albums"
        response = requests.request("GET", url, params=querystring)        
        return response.json()
    else:
        return {"articles": ["Wrong input format"]}
