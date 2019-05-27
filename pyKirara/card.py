import requests
from functools import lru_cache

from .client import Kirara
from .enums import enum, attributes
from .errors import CategoryNotFound

class Card(Kirara):
    """
    Represents a Card and its data

    Attributes
    ----------
    card_id : int
        The card's card id

    album_id : int
        The card's album id

    type : str
        The card's type (Cool, Cute, Passion, Office)

    image : str
        The card's image API link

    has_spread : bool
        True if the card has a spread image, otherwise false

    icon : str
        The card's icon link    

    chara_id : int
        The card's character id

    evo_id : int
        The card's evolution id of transformed card

    evo_type : int
        The card's evolution rarity type (From R to SSR)

    grow_type : int
        An integer that represents a boolean value, checks if card can grow or not

    name : str
        The card's name

    title : str
        The card's untranslated title

    open_dress_id : int
        The card's model id

    place : int
        The card's place value

    pose : int
        The card's sprite number

    series_id : int
        The evolution chain id of the card

    skill_id : int
        The card's skill id

    rarity : dict
        Represents the card's rarity data in dict form

    min_vocal : int
        The card's minimum vocal value

    max_vocal : int
        The card's maximum vocal value

    bonus_vocal : int
        The card's bonus vocal value

    min_dance : int
        The card's minimum dance value

    max_dance : int
        The card's maximum dance value

    bonus_dance : int
        The card's bonus dance value

    min_visual : int
        The card's minimum visual value

    max_visual : int
        The card's maximum visual value

    bonus_visual : int
        The card's bonus visual value

    min_hp : int
        The card's minimum health value

    max_hp : int
        The card's maximum health value

    bonus_hp : int
        The card's bonus health value

    """
    def __init__(self, card_id: int):
        super().__init__()
        self._data(card_id)
        self.card_id = card_id

    @lru_cache(maxsize=None)
    def _data(self, card_id):
        card_data = self.get('card_t/{0}'.format(card_id))['result'][0]

        self.album_id = card_data['album_id']
        self.type = enum(attributes, card_data['attribute'])
        self.image = card_data['card_image_ref']
        self.has_spread = card_data['has_spread']
        self.icon = card_data['icon_image_ref']
        self.chara_id = card_data['chara_id']
        self.evo_id = card_data['evolution_id']
        self.evo_type = card_data['evolution_type']
        self.grow_type = card_data['grow_type']
        self.name = card_data['name']
        self.title = card_data['title']
        self.open_dress_id = card_data['open_dress_id']
        self.place = card_data['place']
        self.pose = card_data['pose']
        self.series_id = card_data['series_id']
        self.skill_id = card_data['skill_id']
        self.rarity = card_data['rarity']

        self.min_vocal = card_data['vocal_min']
        self.max_vocal = card_data['vocal_max']
        self.bonus_dance = card_data['bonus_dance']

        self.min_dance = card_data['dance_min']
        self.max_dance = card_data['dance_max']
        self.bonus_dance = card_data['bonus_dance']

        self.min_visual = card_data['visual_min']
        self.max_visual = card_data['visual_max']
        self.bonus_visual = card_data['bonus_visual']

        self.min_hp = card_data['hp_min']
        self.max_hp = card_data['hp_max']
        self.bonus_hp = card_data['bonus_hp']

    def get_skill(self):
        """Gets skill information via the card's skill_id

        Returns
        -------
        str
            Description of the skill.
        """
        skill = self.get('skill_t/{0}'.format(self.skill_id))['result'][0]['explain_en']

        return skill

    def min_max_stats(self, stat: str, level: int):
        """Calculates the value of a stat in a specific level
    
        Returns
        -------
        int
            Value of stat in specified level
        """
        if stat == 'dance':
            dance_formula = self.min_dance + (self.max_dance - self.min_dance) * (level/self.rarity['base_max_level'])

            return round(dance_formula)

        elif stat == 'visual':
            visual_formula = self.min_visual + (self.max_visual - self.min_visual) * (level/self.rarity['base_max_level'])

            return round(visual_formula)

        elif stat == 'vocal':
            vocal_formula = self.min_vocal + (self.max_vocal - self.min_vocal) * (level/self.rarity['base_max_level'])

            return round(vocal_formula)

    def save_image(self, category, save=False):
        """Save images in a file like object or just the link

        Parameters
        -------
        category : str
            Which image to save (card, icon, spread, transparent, puchi)

        save : bool, optional
            Decided whether to save the image as a  file-like object or just the link
            (Default is False, which gets the image link)

        Returns
        -------
        link : str
            Link to the image

        file : bytes
            The image in a file-like object
        """
        categories = {
            'card': self.image,
            'icon': self.icon,
            'spread': f"https://hidamarirhodonite.kirara.ca/spread/{self.card_id}.png",
            'transparent': f"https://hidamarirhodonite.kirara.ca/chara2/{self.chara_id}/{self.pose}.png",
            'puchi': f"https://hidamarirhodonite.kirara.ca/puchi/{self.chara_id}.png"            
        }

        if category in categories:
            url = categories.get(category)
            if save:
                
                response = requests.get(url, stream=True)

                return response
            else:
                return url
                        
        else:
            raise CategoryNotFound('category must be either card, spread, transparent or puchi')