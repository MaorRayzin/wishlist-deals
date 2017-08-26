from bs4 import BeautifulSoup
import requests

from steam_wishlist.consts import BEAUTIFUL_SOUP_HTML_PARSER, STEAM_PAGE_HTML_ITEM_CLASS, \
    STEAM_PAGE_HTML_ID_PREFIX_COUNT, STEAM_PAGE_HTML_ITEM_NAME, STEAM_PAGE_HTML_ID, STEAM_PAGE_HTML_ITEM_IMG_SRC, \
    STEAM_PAGE_HTML_ITEM_IMG


class Scrapper:

    def __init__(self, profile_wishlist_url):
        self.wishlist_url = profile_wishlist_url

    @staticmethod
    def __get_wishlist_html_page(wishlist_url):
        r = requests.get(wishlist_url)
        if r.status_code == requests.codes.ok:
            return r.content
        else:
            return None

    def get_wishlist(self):
        wishlist_doc = self.__get_wishlist_html_page(self.wishlist_url)
        soup = BeautifulSoup(wishlist_doc, BEAUTIFUL_SOUP_HTML_PARSER)
        item_list = []

        rows = soup.find_all(class_=STEAM_PAGE_HTML_ITEM_CLASS)
        for item in rows:
            name = item.find(class_=STEAM_PAGE_HTML_ITEM_NAME).string
            thumbnail = item.find(STEAM_PAGE_HTML_ITEM_IMG).get(STEAM_PAGE_HTML_ITEM_IMG_SRC)
            id = item[STEAM_PAGE_HTML_ID][STEAM_PAGE_HTML_ID_PREFIX_COUNT:]
            item_list.append({'id': str(id),
                              'name': name,
                              'img': thumbnail})
        return item_list

