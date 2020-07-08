import requests
import json
import time

__author__ = 'washington'


while True:
    print(time.ctime())
    requisi = requests.get('https://economia.awesomeapi.com.br/json/all')
    cambio = json.loads(requisi.text)
    print("Dolar:",cambio['USD'].setdefault("high"))
    print("Euro:",cambio['EUR'].setdefault("high"))
    print("Bitcoin",cambio['BTC'].setdefault('high'))
    print()
    time.sleep(30)



