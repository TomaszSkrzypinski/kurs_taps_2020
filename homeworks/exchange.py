import requests
from datetime import datetime
import time


def exchange_rate_checker():
    d = datetime.now()
    request = requests.get('https://api.exchangeratesapi.io/latest?symbols=PLN')
    print(request.text)
    print(d.hour, ':', d.minute, ':', d.second)
    duration = datetime.now() - d
    print(duration.microseconds)


def decor(function):
    def inside_function():
        print('---------------------------')
        time.sleep(15)
        return function
    return inside_function()


while True:
    decor(exchange_rate_checker())
