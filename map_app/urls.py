from django.conf.urls import url
from . import views
from map_app.models import AreaLocation, Rest, Store, GasStation

urlpatterns = [
		url(r'^$', views.home, name='home'),
		url(r'^search/$', views.area_search, name='area_search'),
]