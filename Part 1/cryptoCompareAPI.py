# with help of for loops or editing URL, all data can be collected
# because there is limit for free users I could not choose this method

def for_API():
    import requests as r
    import json
    import time
    from datetime import datetime

    # file paths and URL are declared
    key_fp = "/Users/emircanerol/Desktop/Lessons/YZV211/Assignments/Assignment1/key.txt"
    URL = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USDT&api_key={}"
    csv = "/Users/emircanerol/Desktop/YZV211/Assignments/Assignment1/BTCUSDT_minute.csv"

    # key is saved
    with open(key_fp, 'r') as f:
        key = f.read()

    # with GET, response received
    resp = r.get(URL.format(key))

    # response is converted and edited
    price = resp.text
    price = json.loads(price)
    price["USDT"] = str("%.2f"%price["USDT"])

    # get time
    now = datetime.now()
    current_time = now.strftime("%d/%m/%Y %H:%M:%S")
    unix = int(time.time())

    file = open('BTCUSD.csv', 'w')
    titles = ['unix', 'date', 'price']
    file.write(','.join(titles) + '\n')
    file.write(','.join([str(unix), str(current_time), str(price['USDT'])]) + '\n')
    file.close()
