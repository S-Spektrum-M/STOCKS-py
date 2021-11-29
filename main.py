import requests
uri = ''

def init(url):
    global uri
    uri = url

def short(ticker):
    a = requests.get(f'{uri}/api/short?id={ticker}').json()
    if 'error' not in a.keys():
        return a
    else:
        return a["error"]

def long(ticker):
    a = requests.get(f'{uri}/api/long?id={ticker}').json()
    if 'error' not in a.keys():
        return a
    else:
        return a["error"]
