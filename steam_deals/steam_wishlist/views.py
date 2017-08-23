from rest_framework.response import Response
from rest_framework.views import APIView
from .wishlist_helpers import get_steam_wishlist




class Wishlist(APIView):

    def get(self, request, steam_id):
        wishlist = get_steam_wishlist(steam_id)
        return Response(wishlist)