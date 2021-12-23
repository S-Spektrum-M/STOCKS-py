import requests
uri = str()

def init(url):
    global uri
    uri = f'http://{url}'

def short(ticker):
    a = requests.get(f'{uri}/api/short?id={ticker}').json()
    if 'error' not in a.keys():
        return [
            float(a['lower']),
            float(a['upper'])
        ]
    else:
        return a["error"]

def long(ticker):
    a = requests.get(f'{uri}/api/long?id={ticker}').json()
    if 'error' not in a.keys():
        return [
            a['lower'],
            a['upper']
        ]
    else:
        return a["error"]

def current_price(ticker) -> float:
    a = requests.get(f'{uri}/api/current?id={ticker}').json()
    if 'error' not in a.keys():
        return float(a['current_price'])
    else:
        return a["error"]
