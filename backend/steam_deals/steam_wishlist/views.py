from rest_framework.response import Response
from rest_framework.views import APIView
from .wishlist_helpers import *


class Wishlist(APIView):
    def get(self, request, steam_id):
        wishlist = get_steam_wishlist(steam_id)
        return Response(wishlist)


class HLTB(APIView):
    def get(self, request, game_steam_id):
        hltb_info = get_hltb_info(game_steam_id)
        return Response(hltb_info)


class CheapSharkGamesDeals(APIView):
    def get(self, request):
        steam_app_ids = request.GET.get('steamAppIds')
        game_deals = get_cheapshark_game_deals(steam_app_ids)
        return Response(game_deals)
