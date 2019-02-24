# coding: utf-8

import requests
import json
from .enums import enum, blood_types, constellations, hands
from functools import lru_cache

class KiraraException(Exception):
    def __init__(self, http_status, code, msg):
        self.http_status = http_status
        self.code = code
        self.msg = msg

    def __str__(self):
        return f"http status: {self.http_status} {self.code} - {self.msg}"

class Kirara(object):
    """
    A class that connects to the kirara api

    ...

    Methods
    -------
    internal_call(method, url, payload, params)
        Makes calls to the api

    get(url, args=None, payload=None)
        Does GET http requests    
    """
    max_retries = 10

    def __init__(self, requests_session=True, request_timeout=None):
        self.prefix = 'https://starlight.kirara.ca/api/v1/'
        self.request_timeout = request_timeout

        if isinstance(requests_session, requests.Session):
            self._session = requests_session
        else:
            if requests_session:
                self._session = requests.Session()
            else:
                from requests import api
                self._session = api

    def internal_call(self, method, url, payload, params):
        args = dict(params=params)
        args["timeout"] = self.request_timeout
        if not url.startswith('http'):
            url = self.prefix + url

        if payload:
            args["data"] = json.dumps(payload)

        r = self._session.request(method, url, **args)
        try:
            r.raise_for_status()
        finally:
            r.connection.close()
        if r.text and len(r.text) > 0 and r.text != 'null':
            results = r.json()
            return results
        else:
            return None

    @lru_cache(maxsize=None)
    def get(self, url, args=None, payload=None, **kwargs):
        if args:
            kwargs.update(args)
        reconnect = self.max_retries
        while reconnect > 0:
            try:
                return self.internal_call('GET', url, payload, kwargs)
            except Exception as e:
                raise
                print('exception', str(e))

    # DEFUNCT FOR NOW
    # @lru_cache(maxsize=None)
    # def post(self, url ,load=None):
    #    payload = f"[\{load"\]".encode('utf-8')
    #    result = requests.request("POST", self.prefix + url, data=payload)
    #    return result.text

class Info(Kirara):
    """
    Represents the API's info
    """

    def __init__(self):
        super().__init__()
        self._data()

    def _data(self):
        self.truth = self.get('info')['truth_version']
        self._api_major = self.get('info')['api_major']
        self._api_revision = self.get('info')['api_revision']
        
class Gacha(Kirara):
    """
    Represents gacha information
    ...

    Attributes
    ----------
    gacha : int
        a value that represents the gacha's position 
    """
    def __init__(self, gacha: int):
        super().__init__()
        self._gacha(gacha)

    def _gacha(self, gacha):
        _gacha = self.get('happening/now')['gachas'][gacha]

        self.id = _gacha['id']
        self.name = _gacha['name']
        self.start_date = _gacha['start_date']
        self.end_date = _gacha['end_date']
        self.type = _gacha['type']
        self.subtype = _gacha['subtype']
        self.rates = _gacha['rates']
        
class Idol(Kirara):
    """
    Represents an idol and her data
    ...

    Attributes
    ----------
    char_id : int
        the idol's characted id
    """
    def __init__(self, char_id: int):
        super().__init__()
        self._data(char_id)

    @lru_cache(maxsize=None)
    def _data(self, char_id):
        char_data = self.get(f'char_t/{char_id}')['result'][0]

        self.age = char_data['age']
        self.bday = char_data['birth_day']
        self.bmonth = char_data['birth_month']
        self.btype = enum(blood_types, char_data['blood_type'])
        self.bust = char_data['body_size_1']
        self.waist = char_data['body_size_2']
        self.hip = char_data['body_size_3']
        self.chara_id = char_data['chara_id']
        self.horoscope = enum(constellations, char_data['constellation'])
        self.conventional = char_data['conventional']
        self.favorite = char_data['favorite'] # NOTE: In Japanese due to read_tl not returning english
        self.hand = enum(hands, char_data['hand'])
        self.height = char_data['height']

        if char_id == 134: # Because Anzu has unknown sizes
            self.bust = "???"
            self.waist = "???"
            self.hip = "???"

# ToDo:
# Add object lists
# Add card objects
# Optimize code