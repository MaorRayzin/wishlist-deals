from bs4 import BeautifulSoup
import requests

from steam_wishlist.consts import BEAUTIFUL_SOUP_HTML_PARSER, STEAM_PAGE_HTML_ITEM_CLASS, \
    STEAM_PAGE_HTML_ID_PREFIX_COUNT, STEAM_PAGE_HTML_ITEM_NAME, STEAM_PAGE_HTML_ID


class Scrapper:

    def __init__(self, profile_wishlist_url):
        self.wishlist_url = profile_wishlist_url

    def __get_wishlist_html_page(self):
        r = requests.get(self.wishlist_url)
        if r.status_code == requests.codes.ok:
            self.wishlist_doc = r.content

    def get_wishlist(self):
        self.__get_wishlist_html_page()
        soup = BeautifulSoup(self.wishlist_doc, BEAUTIFUL_SOUP_HTML_PARSER)
        item_list = []

        rows = soup.find_all(class_=STEAM_PAGE_HTML_ITEM_CLASS)
        for item in rows:
            name = item.find(class_=STEAM_PAGE_HTML_ITEM_NAME).string
            id = item[STEAM_PAGE_HTML_ID][STEAM_PAGE_HTML_ID_PREFIX_COUNT:]
            item_list.append({'id': str(id),
                              'name': name})
        return item_list

