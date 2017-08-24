from rest_framework.response import Response
from rest_framework.views import APIView
from .wishlist_helpers import *


class Wishlist(APIView):
    def get(self, request, steam_id):
        wishlist = get_steam_wishlist(steam_id)
        return Response(wishlist)


class CheapSharkGameDetails(APIView):
    def get(self, request, steam_app_id):
        game_details = get_cheapshark_game_details(steam_app_id)
        return Response(game_details)


class CheapSharkGamesDeals(APIView):
    def get(self, request, cheapshark_game_ids):
        game_deals = get_cheapshark_games_deals(cheapshark_game_ids)
        return Response(game_deals)
