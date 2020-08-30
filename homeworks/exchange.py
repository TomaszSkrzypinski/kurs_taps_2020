import requests
from datetime import datetime
import time

from selenium.common.exceptions import TimeoutException


def exchange_rate_checker():
    try:
        d = datetime.now()
        request = requests.get('https://api.exchangeratesapi.io/latest?symbols=PLN')
        rate = request.json()
        print(rate['rates'])
        print('Data i godzina: ', d.year, '.', d.month, '.', d.day, d.hour, ':', d.minute, ':', d.second)
        duration = datetime.now() - d
        duration_in_ms = int(duration.microseconds / 1000)
        print('Czas trwania zapytania :',duration_in_ms , 'ms')

    except TimeoutException:
        print('Timeout Exception')


def decor(function):
    def inside_function():
        print('---------------------------')
        return function
    return inside_function()


while True:
    decor(exchange_rate_checker())
    time.sleep(15)
