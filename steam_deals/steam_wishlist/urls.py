from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'(?P<steam_id>\d+)$', views.Wishlist.as_view())
]
