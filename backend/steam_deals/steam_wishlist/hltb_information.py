from igdb_api_python import igdb
from django.conf import settings
from requests import codes as http_codes
from steam_wishlist.consts import IGDB_NAME, IGDB_HLTB_STATS, IGDB_FIELDS_PARAM, IGDB_SEARCH_PARAM


class HLTB:
    def __init__(self, wishlist):
        self.wishlist_games_list = wishlist
        self.igdb_client = igdb.igdb(settings.IGDB_API_KEY)

    def get_hltb_info_for_wishlist(self):
        for game in self.wishlist_games_list:
            result = self.igdb_client.games(
                {
                    IGDB_SEARCH_PARAM: str(game.get('name')),
                    IGDB_FIELDS_PARAM: [IGDB_HLTB_STATS]
                })

            if result.status_code == http_codes.ok:
                game['hltb'] = result.body[0].get('time_to_beat', None)

        return self.wishlist_games_list
