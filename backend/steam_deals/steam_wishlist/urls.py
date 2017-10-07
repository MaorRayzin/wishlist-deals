from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<steam_id>\d+)$', views.Wishlist.as_view()),
    url(r'^deals/(?P<steam_app_id>\d+)$', views.CheapSharkGamesDeals.as_view())
]
