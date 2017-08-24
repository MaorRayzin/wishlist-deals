WISHLIST_SCRAPPER_URL = 'https://www.foxslash.com/apps/steamchecker/wishlist.php?url=http://steamcommunity.com/profiles/{0}/wishlist'

CHEAP_SHARK_API_BASE_URL = 'http://www.cheapshark.com/api/1.0{0}'

CHEAP_SHARK_API_BASE_GAME_URL = CHEAP_SHARK_API_BASE_URL.format('/games{0}')
CHEAP_SHARK_API_BASE_DEAL_URL = CHEAP_SHARK_API_BASE_URL.format('/deals{0}')

CHEAP_SHARK_API_GET_GAME_DETAILS_URL = CHEAP_SHARK_API_BASE_GAME_URL.format('?steamAppID={0}')
CHEAP_SHARK_API_GET_GAMES_DEALS_URL = CHEAP_SHARK_API_BASE_GAME_URL.format('?ids={0}')
