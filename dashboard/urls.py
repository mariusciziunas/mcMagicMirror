from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^weather-forecast', views.get_weather_forecast, name='get_weather_forecast'),
    url(r'^calendar', views.get_calendar, name='get_calendar'),
    url(r'^train-departures', views.get_train_departures, name='get_train_departures'),
    url(r'^bus-arrivals', views.get_bus_arrivals, name='get_bus_arrivals'),
    url(r'^technology-news', views.get_news_technology, name='get_news_technology'),
    url(r'^world-news', views.get_news_world, name='get_news_world'),
    url(r'^sport-news', views.get_news_sport, name='get_news_sport'),
    url(r'^alarm-status', views.alarm_status, name='alarm_status'),
    url(r'^alarm', views.video, name='video'),
    url(r'^disable-alarm', views.disable_alarm, name='disable_alarm'),
    url(r'^notes', views.notes, name='notes'),
    url(r'^', views.index, name='dashboard')

]