import requests
import json
from .consts import WISHLIST_SCRAPPER_URL


def get_steam_wishlist(steam_id):
    scrap_req = requests.get(WISHLIST_SCRAPPER_URL.format(steam_id))
    wishlist = json.loads(scrap_req.text)
    if wishlist:
        return wishlist
    else:
        return {}


def get_game_details(games_list):
    pass

def get_game_deal(game):
    pass