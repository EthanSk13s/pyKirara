# coding: utf-8

import requests
import json
from functools import lru_cache
from .enums import enum, blood_types, constellations, hands, home_towns


class KiraraException(Exception):
    def __init__(self, http_status, code, msg):
        self.http_status = http_status
        self.code = code
        self.msg = msg

    def __str__(self):
        return f"http status: {self.http_status} {self.code} - {self.msg}"

class Kirara(object):
    """A class that connects to the kirara api

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
        """Makes HTTP requests
        
        Parameters
        ----------
        method : str
            method of making HTTP requests ('GET', 'POST', etc.)

        url : str
            The url to make HTTP requests to

        payload : str
            Any additional parameters to pass

        params : dict
            Parameters to pass to a dict

        Returns
        ----------
        dict
            The result of the request in dict format
        """
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
        """Make GET requests
        
        Parameters
        ----------
        url : str
            The url to the api (excluding the prefix url)

        args : dict
            Pass additional args

        payload : str
            Pass any additional parameters to request

        Returns
        ----------
        dict
            The result of the GET request
        """
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

    Attributes
    ----------
    truth : str
        The game's (Deresute) truth version

    api_major : int
        The API's version major

    api_revision : int
        The API's revision number        

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

    Attributes
    ----------
    gacha : int
        A value that represents the gacha's position

    id : int
        The gacha's id

    name : int
        The gacha's name in japanese

    start_date : UNIX-datetime
        The gacha's start date

    end_date : UNIX-datetime    
        The gacha's end date

    type : int
        The gacha type

    subtype : int
        The gacha sub-type

    rates : dict
        The weighted rates for the gacha

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