from functools import lru_cache

from .client import Kirara
from .enums import enum, attributes

class Card(Kirara):
    def __init__(self, card_id: int):
        super().__init__()
        self._data(card_id)

    @lru_cache(maxsize=None)
    def _data(self, card_id):
        card_data = self.get('card_t/{0}'.format(card_id))['result'][0]

        self.album_id = enum(attributes, card_data['album_id'])
        self.bonus_dance = card_data['bonus_dance']
        self.bonus_hp = card_data['bonus_hp']
        self.bonus_visual = card_data['bonus_visual']
        self.card_image = card_data['card_image_ref']
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

# TODO:
# Finish up class
# Add get_skill function
# Documentation