import requests

def get_btc_usd():
    url = "https://yobit.net/api/3/ticker/btc_usd"
    res = requests.get(url).json()
    price_btc = res["btc_usd"]["last"]
    return str(round(price_btc, 2)) + " usd"
print(get_btc_usd())

def get_usd_rur():
    url = "https://yobit.net/api/3/ticker/usd_rur"
    res = requests.get(url).json()
    price_btc = res["usd_rur"]["last"]
    return str(round(price_btc, 2)) + " rur"
print(get_usd_rur())
