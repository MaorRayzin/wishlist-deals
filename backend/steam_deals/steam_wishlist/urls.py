from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<steam_id>\d+)$', views.Wishlist.as_view()),
    url(r'^hltb/(?P<game_steam_id>\d+)$', views.HLTB.as_view()),
    url(r'^deals$', views.CheapSharkGamesDeals.as_view())
]
