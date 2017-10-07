import requests
import json

from steam_wishlist.consts import STEAM_WISHLIST_URL, \
    CHEAP_SHARK_API_GET_GAMES_DEALS_URL, CHEAP_SHARK_API_GET_DEAL_DETAILS_URL
from steam_wishlist.wishlist_scraper import Scrapper
from steam_wishlist.hltb_information import HLTB


def get_hltb_info(game_steam_id):
    hltb_client = HLTB(game_steam_id)
    return hltb_client.get_hltb_info_for_wishlist()


def get_steam_wishlist(steam_id):
    scrapper = Scrapper(STEAM_WISHLIST_URL.format(steam_id))
    wishlist = scrapper.get_wishlist()
    if wishlist:
        return wishlist
    else:
        return []


def get_cheapshark_cheapest_price_ever(deals):
    # We assume there's at least one deal
    # It seems like the cheapest price is actually global and not per deal, so it's enough to check just one of them
    deal_id = deals[0]['dealID']
    req = requests.get(CHEAP_SHARK_API_GET_DEAL_DETAILS_URL.format(deal_id))
    parsed_deal = json.loads(req.text)
    return parsed_deal['cheapestPrice']['price']


def get_cheapshark_games_deals(steam_app_id):
    req = requests.get(CHEAP_SHARK_API_GET_GAMES_DEALS_URL.format(steam_app_id))
    req = json.loads(req.text)
    game_deals = {}
    game_deals['cheapestPriceEver'] = get_cheapshark_cheapest_price_ever(req)
    game_deals['deals'] = []
    for deal in req:
        parsed_deal = {}
        parsed_deal['dealID'] = deal['dealID']
        parsed_deal['storeID'] = deal['storeID']
        parsed_deal['salePrice'] = deal['salePrice']
        parsed_deal['normalPrice'] = deal['normalPrice']
        parsed_deal['savings'] = deal['savings']
        game_deals['deals'].append(parsed_deal)
    return json.dumps(game_deals)
