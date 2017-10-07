from igdb_api_python import igdb
from django.conf import settings
from requests import codes as http_codes
from steam_wishlist.consts import IGDB_EXTERNAL_FILTER_PARAM, IGDB_FIELDS_PARAM, IGDB_FILTERS, IGDB_HLTB_TERM, \
    HLTB_TIME_CONVERT_STRING


class HLTB:
    def __init__(self, game_steam_id):
        self.game_steam_id = game_steam_id
        self.igdb_client = igdb.igdb(settings.IGDB_API_KEY)

    @staticmethod
    def __convert_seconds_to_full_time(seconds):
        minutes, s = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return HLTB_TIME_CONVERT_STRING % (hours, minutes, s)

    def get_hltb_info_for_wishlist(self):
        result = self.igdb_client.games(
            {
                IGDB_FILTERS:
                    {
                        IGDB_EXTERNAL_FILTER_PARAM: self.game_steam_id
                    },
                IGDB_FIELDS_PARAM: IGDB_HLTB_TERM
            })
        time_to_beat = result.body[0].get(IGDB_HLTB_TERM)
        if result.status_code == http_codes.ok:
            for ttb in time_to_beat:
                time_to_beat[ttb] = HLTB.__convert_seconds_to_full_time(time_to_beat[ttb])

            response = {
                'steam_game_id': self.game_steam_id,
                IGDB_HLTB_TERM: time_to_beat
            }
        else:
            response = None

        return response
