import requests
import json
from .consts import *


def get_steam_wishlist(steam_id):
    scrap_req = requests.get(WISHLIST_SCRAPPER_URL.format(steam_id))
    wishlist = json.loads(scrap_req.text)
    if wishlist:
        return wishlist
    else:
        return {}


def get_cheapshark_game_details(steam_app_id):
    req = requests.get(CHEAP_SHARK_API_GET_GAME_DETAILS_URL.format(steam_app_id))
    return json.loads(req.text)


def get_cheapshark_games_deals(cheapshark_game_ids):
    req = requests.get(CHEAP_SHARK_API_GET_GAMES_DEALS_URL.format(cheapshark_game_ids))
    return json.loads(req.text)
