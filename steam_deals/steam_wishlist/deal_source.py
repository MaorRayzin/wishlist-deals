

class CheapSharkAPI:
    def __init__(self):
        pass

    def __filter_string_builder(self, args):
        filter_string = '?'

        for k,v in args:
            filter_string += '{0}={1}&'.format(k,v)

        return filter_string

    def game(self, title=None, store_id=None, steam_store_id=None):
        pass

    def deal(self, game_id=None, steam_store_id=None, title=None):
        pass


class DealEngine:
    def __init__(self):
        self.sources = [CheapSharkAPI]