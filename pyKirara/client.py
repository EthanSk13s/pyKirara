# coding: utf-8

import requests
import json
from functools import lru_cache

import idol
import card
from .enums import enum, blood_types, constellations, hands, home_towns, rarities
from .errors import CategoryNotFound



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

    def __init__(self, requests_session=True, request_timeout=10):
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

    def get_idol(self, idol_id: int):
        data = self.get(f"char_t/{idol_id}")

        return idol.Idol(data['result'][0])
        
    def get_card(self, card_id: int):
        data = self.get(f"card_t{card_id}")

        return card.Card(data['result'][0])

    def get_image(self, card: 'Card', category='card'):
        categories = {
            'card': card.image,
            'icon': card.icon,
            'spread': card.spread,
            'sprite': card.sprite,
        }

        if category in categories:
            image = categories.get(category)

            response = self._session.get(image)

            return response

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

    name : str
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

class Event(Kirara):
    """
    Represents event info

    Attributes
    -------
    event : int
        Event index number in 'happening/now' endpoint

    id : int
        The event's id

    name : str
        Event name

    start_date : datetime obj
        Event start date

    end_date : datetime obj
        Event end date

    result_end_date : datetime obj
        The time left for the Event until it ends
    """

    def __init__(self, event: int):
        super().__init__()
        self._event(event)

    def _event(self, event):
        _event = self.get('happening/now')['events'][event]

        self.id = _event['id']
        self.name = _event['name']
        self.start_date = _event['start_date']
        self.end_date = _event['end_date']
        self.result_end_date = _event['result_end_date']

def get_id(category, name, card_rarity, position=None):
    """
    Returns a specific id of an item

    Parameters
    ----------
    category : str
        A specific category to use, i.e 'char_t', or 'card_t'

    name : str
        This is the name of an idol

    Returns
    -------
    int
        The specific ID matching the name given.

    list
        If the category is card, returns a list of cards matching the name
    """
    cat_list = Kirara().get(f'list/{category}')['result']
    rarity = enum(rarities, card_rarity)
    card_list = []

    for index, code in enumerate(cat_list):
        if category == 'char_t':
            if name == cat_list[index]['conventional']:
            
                return int(cat_list[index]['chara_id'])
        
        elif category == 'card_t':
            if name == cat_list[index]['conventional']:
                if int(rarity) == int(cat_list[index]['rarity_dep']['rarity']):
                    card_list.append(int(cat_list[index]['id']))
        else:
            
            raise CategoryNotFound("Invalid category, use char_t, or card_t")

    return card_list

        

def happening_list(category):
    """
    Returns a list of event objects that are currently happening

    Parameters
    -------
    category : str
        A category to use from (use either 'events' or 'gachas')

    Returns
    -------
    list
        A list of event or gacha objects that are occuring currently

    None
        If there is nothing ongoing
    """
    categories = {
        'events': Kirara().get(f"happening/now")['events'],
        'gachas': Kirara().get(f"happening/now")['gachas']
    }
    
    happening_now = []

    if category in categories:
        got = categories.get(category)

        for index, event in enumerate(got):
            if category == 'events':

                happening_now.append(Event(index))
            else:
                for gacha, event in enumerate(got): # I don't know why you have to iterate again, maybe Im dumb

                    happening_now.append(Gacha(gacha))

            return happening_now
    else:
        raise CategoryNotFound("Invalid Category, use 'events' or 'gachas'")
