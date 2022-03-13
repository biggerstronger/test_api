# https://developers.lingvolive.com/ru-ru/Help
from typing import List

import requests
from requests import Response

API_KEY = 'NWVjOTRhMzUtODU1MC00ZmFhLWExMjQtOWJiNmIxOGNkNTY4Ojc1ZGM1YTZhYjgyMTRiNjFhY2I3OTE5NzFlZTgwZjQ5'
APP_KEY = ''
AUTH_URL = 'https://developers.lingvolive.com/api/v1.1/authenticate'
TRANSLATE_URL = 'https://developers.lingvolive.com/api/v1/Minicard'
EN = '1033'
RU = '1049'


def authotization() -> int:
    global APP_KEY
    auth_header = {
        'Authorization': 'Basic ' + API_KEY
    }
    auth = requests.post(AUTH_URL, headers=auth_header)
    APP_KEY = auth.text
    return auth.status_code


def translate_en_ru(word: str) -> str:
    translate_header = {
        'Authorization': 'Bearer ' + APP_KEY,
    }
    params = {
        'text': word,
        'srcLang': EN,
        'dstLang': RU
    }
    t = requests.get(TRANSLATE_URL, headers=translate_header, params=params).json()
    try:
        translation = t['Translation']['Translation']
        return translation.split(',')[0] if type(translation.split(',')) == list else translation
    except:
        print('Not found')
    return 'error'


def translate_ru_en(word: str) -> str:
    translate_header = {
        'Authorization': 'Bearer ' + APP_KEY,
    }
    params = {
        'text': word,
        'srcLang': RU,
        'dstLang': EN
    }
    t = requests.get(TRANSLATE_URL, headers=translate_header, params=params).json()
    try:
        translation = t['Translation']['Translation']
        return translation.split(',')[0] if type(translation.split(',')) == list else translation
    except:
        print('Not found')
        return 'error'


if __name__ == '__main__':
    print(authotization())
    t_en = translate_en_ru('dog')
    print(t_en)
    print(translate_ru_en(t_en))
