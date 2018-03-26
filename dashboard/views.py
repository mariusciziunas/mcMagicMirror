# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import coreapi
from django.http import JsonResponse
from django.shortcuts import render
import itertools
from datetime import datetime
from datetime import timedelta
from pyicloud import PyiCloudService
from .TFL import TFL
from .national_rail import national_rail
from .News import News
import operator
from .models import Config, State, Note
import configparser
import pigpio
import RPi.GPIO as GPIO

def index(request):
    return render(request, 'dashboard/index.html')

def video(request):
    turn_on_led(request)
    return render(request, 'dashboard/youtube_video.html')

def alarm_status(request):
    state = request.GET.get('state', 'alarm_active')
    response = {}
    try:
        response['status'] = {}
        state = State.objects.get(key=state)
        response['status']['key'] = state.key
        response['status']['value'] = int(state.value) == 1
    except State.DoesNotExist:
        print('state [' + state + '] does not exist in the DB')
    return JsonResponse(response)

def turn_on_led(request):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24,GPIO.OUT)
    GPIO.output(24,100)
    response = {}
    return JsonResponse(response)

def turn_off_led(request):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24,GPIO.OUT)
    GPIO.output(24,False)
    GPIO.cleanup()
    response = {}
    return JsonResponse(response)

def notes(request):
    response = {}
    response['notes'] = []
    try:
        notes =  Note.objects.all()
        for note in notes:
            new_note = {}
            new_note['id'] = note.pk
            new_note['text'] = note.text
            response['notes'].append(new_note)
    except Note.DoesNotExist:
        print('There are no notes')
    return JsonResponse(response)

def disable_alarm(request):
    alarm_state = 'alarm_active'
    state = State.objects.get(key = alarm_state)
    state.value = 0
    state.last_updated = datetime.now()
    state.save()
    turn_off_led(request)
    response = {}
    response['status'] = {}
    response['status']['key'] = alarm_state
    response['status']['value'] = 0

    return JsonResponse(response)

def get_news_world(request):
    config = configparser.ConfigParser()
    config.read('./config.ini')
    sources = config['DEFAULT']['world.news.sources']
    count = int(config['DEFAULT']['world.news.count'])
    return get_news(sources, count)

def get_news_sport(request):
    config = configparser.ConfigParser()
    config.read('./config.ini')
    sources = config['DEFAULT']['sport.news.sources']
    count = int(config['DEFAULT']['sport.news.count'])
    return get_news(sources, count)

def get_news_technology(request):
    config = configparser.ConfigParser()
    config.read('./config.ini')
    sources = config['DEFAULT']['technology.news.sources']
    count = int(config['DEFAULT']['technology.news.count'])
    return get_news(sources, count)

def get_news(sources, count):
    api_key = Config.objects.get(key='newsapi.key')
    news_api = News(api_key.value)
    response = []
    for source in sources.split(','):
        news = news_api.get_news_by_source(source)
        news = news[:count]
        response.extend(news)
    result = {}
    result['news'] = response
    return JsonResponse(result)

def get_calendar(request):
    config = configparser.ConfigParser()
    config.read('./config.ini')
    days_to_display = int(config['DEFAULT']['icloud.calendar.days_to_display'])
    return JsonResponse(get_icloud_events(days_to_display))

def get_train_departures(request):
    stationCode = request.GET.get('stationCode', 'BFD')
    rowCount = int(request.GET.get('rowCount', 20))
    return JsonResponse(get_trains(stationCode, rowCount))

def get_bus_arrivals2(request):
    app_id = Config.objects.get(key='tfl.id')
    app_key = Config.objects.get(key='tfl.key')
    api = TFL(app_id=app_id, app_key=app_key)
    # waterman_to_kew_bus_arrivals = api.get_arrivals_for_stop_point('490006297W')
    # albany_to_ealing_bus_arrivals = api.get_arrivals_for_stop_point('490003137X')
    # default value is waterman to kew arrivals
    response = api.get_arrivals_for_stop_point(request.GET.get('stopPoint', '490006297W'))
    return JsonResponse(response)

def get_bus_arrivals(request):
    app_id = Config.objects.get(key='tfl.id').value
    app_key = Config.objects.get(key='tfl.key').value
    api = TFL(app_id=app_id, app_key=app_key)
    stopPoints = '490006297W,490003137X'

    response = {}
    response['arrivals'] = []
    for stop_point in stopPoints.split(','):
        response['arrivals'].extend(api.get_arrivals_for_stop_point(stop_point))

    return JsonResponse(response)

def get_trains(stationCode, rowsCount):
    token = Config.objects.get(key='nationalrail.token').value
    trains_api = national_rail('https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx?ver=2017-02-02',
                               token)
    departures = trains_api.get_departure_board(stationCode, rowsCount)
    departures = trains_api.limit_departure_count(departures, 8)
    return departures

def get_icloud_events(days):
    apple_id = Config.objects.get(key='apple.id').value
    password = Config.objects.get(key='apple.password').value
    icloud_api = PyiCloudService(apple_id, password)

    from_dt = datetime.now()
    to_dt = from_dt + timedelta(days=days)
    result = {}
    result['events'] = []
    api_response = {}
    api_response['events'] = icloud_api.calendar.events(from_dt, to_dt)
    for api_event in api_response['events']:
        event = {}
        event['startDate'] = get_date_time(api_event['startDate'])
        event['endDate'] = get_date_time(api_event['endDate'])
        event['title'] = api_event['title']
        event['id'] = api_event['guid']
        result['events'].append(event)
    result['events'].sort(key=operator.itemgetter('startDate'))

    result['events'] = format_events(result['events'])
    return result

def format_events(events):
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    agenda = []
    for event in events:
        formatted_event = event
        day = None
        if (today.date() == event['startDate'].date()):
            day = 'Today'
        elif (event['startDate'].date() == tomorrow.date()):
            day = 'Tomorrow'
        else:
            day = event['startDate'].strftime('%A, %d %b')

        formatted_event['startDate'] = event['startDate'].strftime('%H:%M')
        formatted_event['endDate'] = event['endDate'].strftime('%H:%M')

        is_day_in_agenda = False
        for day_in_agenda in agenda:
            if (day_in_agenda['day'] == day):
                day_in_agenda['events'].append(formatted_event)
                is_day_in_agenda = True

        if (not is_day_in_agenda):
            agenda_item = {}
            agenda_item['day'] = day
            agenda_item['events'] = []
            agenda_item['events'].append(formatted_event)
            agenda.append(agenda_item)

    return agenda


def get_date_time(event):
    return datetime(event[1], event[2], event[3], event[4],
                    event[5])

def get_weather_forecast(request):
    weather_forecast = __get_weather_current()
    weather_forecast.extend(__get_forecast())
    json_result = {}
    json_result['forecast'] = weather_forecast
    return JsonResponse(json_result)

def __get_forecast():
    app_id = Config.objects.get(key='openweather.key').value
    client = coreapi.Client()
    weather_api = client.get(
        'http://api.openweathermap.org/data/2.5/forecast?q=London,uk&units=metric&APPID=' + app_id)
    weather_forecast = []

    for forecast in itertools.islice(weather_api.get('list'), 4):
        weather_forecast.append(__convert_2_api_format(forecast))
    weather_forecast.extend(__get_forecast_for_day(weather_api['list'][5:]))
    # let's remove few elements to nicely fit into the screen
    del weather_forecast[2]
    del weather_forecast[-1]
    return weather_forecast

def __get_weather_current():
    app_id = Config.objects.get(key='openweather.key').value
    client = coreapi.Client()
    api = client.get(
        'http://api.openweathermap.org/data/2.5/weather?q=London,uk&units=metric&APPID=' + app_id)
    result = []
    current_weather = __convert_2_api_format(api)
    result.append(current_weather)
    return result

def __get_forecast_for_day(weather_forecast):
    result = []
    for forecast_item in weather_forecast:
        dt = datetime.fromtimestamp(forecast_item['dt'])
        if dt.hour == 12:
            midday_forecast_item = __convert_2_api_format(forecast_item)
            midday_forecast_item['dt'] = dt.strftime('%a')
            result.append(midday_forecast_item)
    return result

def __convert_2_api_format(forecast):
    forecast_item = {}
    forecast_item['dt'] = datetime.utcfromtimestamp(forecast['dt']).strftime('%H:%M')
    forecast_item['description'] = forecast['weather'][0]['main']
    forecast_item['icon'] = forecast['weather'][0]['icon']
    forecast_item['temp'] = round(forecast['main']['temp'])
    forecast_item['humidity'] = forecast['main']['humidity']
    return forecast_item