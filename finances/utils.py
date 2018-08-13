import requests
from bs4 import BeautifulSoup


proxy_dict_keys = (
    'ip',
    'port',
    'country_code',
    'country',
    'type',
    'google',
    'https',
    'last_checked'
)

PROXY_LIST_URL = 'https://free-proxy-list.net/anonymous-proxy.html'

UNECESSARY_COUNTRIES = ('RU', )


def get_proxy():
    r = requests.get(PROXY_LIST_URL).text
    soup = BeautifulSoup(r, 'html.parser')
    rows = soup.select('table tbody tr')
    for row in rows:
        proxy = {
            k: v.text
            for k, v in dict(zip(proxy_dict_keys, row.select('td'))).items()
            if k not in UNECESSARY_COUNTRIES
        }
        ip = ':'.join((proxy['ip'], proxy['port']))
        yield dict(http=ip, https=ip)


def perform_(some_dict: dict):
    tmp = {}
    for i in some_dict.keys():
        tmp['time'] = i
        tmp.update(some_dict[i])
    return tmp
