from rest_framework.response import Response
from rest_framework.views import APIView
from .wishlist_helpers import *


class Wishlist(APIView):
    def get(self, request, steam_id):
        wishlist = get_steam_wishlist(steam_id)
        return Response(wishlist)


class CheapSharkGamesDeals(APIView):
    def get(self, request, steam_app_id):
        game_deals = get_cheapshark_games_deals(steam_app_id)
        return Response(game_deals)
