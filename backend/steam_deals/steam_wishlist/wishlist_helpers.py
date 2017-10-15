import requests
import json

from steam_wishlist.consts import STEAM_WISHLIST_URL, \
    CHEAP_SHARK_API_GET_GAME_DEALS_URL, CHEAP_SHARK_API_GET_DEAL_DETAILS_URL
from steam_wishlist.wishlist_scraper import Scrapper
from steam_wishlist.hltb_information import HLTB


def get_hltb_info(game_steam_id):
    hltb_client = HLTB([game_steam_id])
    return hltb_client.get_hltb_info_for_wishlist()


def get_steam_wishlist(steam_id):
    scrapper = Scrapper(STEAM_WISHLIST_URL.format(steam_id))
    wishlist = scrapper.get_wishlist()
    if wishlist:
        return wishlist
    else:
        return []


def get_cheapshark_cheapest_price_ever(deals):
    # It seems like the cheapest price is actually global and not per deal, so it's enough to check just one of them
    deal_id = deals[0]['dealID']
    req = requests.get(CHEAP_SHARK_API_GET_DEAL_DETAILS_URL.format(deal_id))
    parsed_deal = json.loads(req.text)
    return parsed_deal['cheapestPrice']['price']


def get_cheapshark_game_deals(steam_app_ids):
    req = requests.get(CHEAP_SHARK_API_GET_GAME_DEALS_URL.format(steam_app_ids))
    cheapshark_deals = json.loads(req.text)

    placeholder_deal_dict = {steam_app_id: [] for steam_app_id in steam_app_ids.split(',')}
    for cheapshark_deal in cheapshark_deals:
        parsed_deal = {'dealID': cheapshark_deal['dealID'], 'storeID': cheapshark_deal['storeID'],
                       'salePrice': cheapshark_deal['salePrice'], 'normalPrice': cheapshark_deal['normalPrice'],
                       'savings': cheapshark_deal['savings']}

        steam_app_id = cheapshark_deal['steamAppID']
        placeholder_deal_dict[steam_app_id].append(parsed_deal)

    return [
        {'steamAppId': steam_app_id, 'deals': deals, 'cheapestPriceEver': get_cheapshark_cheapest_price_ever(deals)}
        for steam_app_id, deals in placeholder_deal_dict.items()]
