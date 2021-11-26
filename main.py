import requests
import json
uri = ''
def init(url):
    global uri
    uri = url

def short(ticker):
    try:
        a = requests.get(f'{uri}/api/short?id={ticker}').json()
        return a
    except Exception as e:
        return {'error': 'bad_id'}

def long(ticker):
    try:
        a = requests.get(f'{uri}/api/long?id={ticker}').json()
        return a
    except Exception as e:
        return {'error': 'bad_id'}
