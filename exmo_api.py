import requests
import json
import  time

while True:
    r = requests.get('https://api.exmo.com/v1/ticker/')
    obj = json.loads(r.text)
    total = []

    for pair in obj:
        all_pair = {
            'pair': pair.lower(),
            'updated': obj[pair]['updated'],
            'last_trade': obj[pair]['last_trade'],
            'high': obj[pair]['high'],
            'low': obj[pair]['low'],
            'avg': obj[pair]['avg'],
            'buy': obj[pair]['buy_price'],
            'sell': obj[pair]['sell_price'],
            'vol_curr': obj[pair]['vol_curr'],
            'vol': obj[pair]['vol'],
            'volatilyty': ((float(obj[pair]['high']) - float(obj[pair]['low'])) * 100) / float(obj[pair]['avg'])
        }
        total.append(all_pair)
    all_pair_json = json.dumps(total)

    for i in total:
        print(i)
    print()

    time.sleep(2)