import json
from requests import get, utils
import datetime as dt


URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
URL2 = 'http://www.cbr.ru/scripts/XML_daily.asp'


def currency_rates(*args):
    """ Request and response from daily_json.asp

       :param args: Tuple of CharCodes of valuta
       :return: date and time and the current exchange rate of the requested currency
       """
    response = get(URL)
    dict_json = json.loads(response.text)
    ans_dict = {}
    ans_dict.setdefault('Date', dict_json.get('Date').split('T')[0])
    for value in args:
        value = value.upper()
        course = dict_json.get('Valute').get(value)
        if course:
            course = course.get('Value')
        ans_dict.setdefault(value, course)
    return ans_dict


def curency_rates_2(*args):
    """ Request and response from XML_daily.asp

    :param args: Tuple of CharCodes of valuta
    :return: date and time and the current exchange rate of the requested currency
    """

    response = get(URL2)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    raw_date_str = content[content.find('Date'): content.find('name')]
    time = str(dt.datetime.now())[11:19]
    date_time = dt.datetime.strptime(raw_date_str + ' ' + time, 'Date="%d.%m.%Y" %H:%M:%S')
    out_data = {'Date: ': str(date_time)}
    for char_code in args:
        char_code = char_code.upper()
        lcl_str_ind_start = content.find(f'<CharCode>{char_code}</CharCode>')
        if lcl_str_ind_start > 0 :
            lcl_str_ind_stop = content.find('</Value>', lcl_str_ind_start)
            lcl_str_ind_start = content.rfind('>', lcl_str_ind_start, lcl_str_ind_stop) + 1
            value = content[lcl_str_ind_start: lcl_str_ind_stop]
            value = float(value.replace(',', '.'))
            out_data.setdefault(char_code, value)
        else:
            out_data.setdefault(char_code)

    return out_data


print(currency_rates('usd', 'eur', 'asdasd'))
print(curency_rates_2('USD', 'eUr', 'asdasd'))


