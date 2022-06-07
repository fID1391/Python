import json
from requests import get
import datetime as dt


URL = 'https://www.cbr-xml-daily.ru/daily_json.js'


def currency_rates(arg):
    """ Request and response from daily_json.asp

       :param arg: Tuple of CharCodes of valuta
       :return: date and time and the current exchange rate of the requested currency
       if CharCode is not found return None
       """
    response = get(URL)
    dict_json = json.loads(response.text)
    data = (dt.datetime.strptime((dict_json.get('Date')), '%Y-%m-%dT%H:%M:%S%z')).strftime('%Y-%m-%d')
    for value in arg:
        value = value.upper()
        course = dict_json.get('Valute').get(value)
        if course:
            nominal = int(course.get('Nominal'))
            course = round(float(course.get('Value')), 2)
            data += f'\n {nominal} {value} - {course} RUB'
        else:
            data += f'\n {value} - {course}'
    return data
