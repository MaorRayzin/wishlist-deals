from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'$', views.Wishlist.as_view())
]
