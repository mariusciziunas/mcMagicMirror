import requests
from datetime import datetime

class TFL(object):
    def __init__(self, app_id, app_key):
        self._app_id = app_id
        self._app_key = app_key
        self._url = "https://api.tfl.gov.uk"

    def get_arrivals_for_stop_point2(self, stop_point):
        response = requests.get(
            self._url + "/StopPoint/" + stop_point + "/arrivals?app_key=" + self._app_key + "&app_id=" + self._app_id)
        result_arrival = {}
        for arrival in response.json():
            line = arrival['lineName']
            if (result_arrival.get(line) == None):
                result_arrival[line] = {}
            result_arrival[line]['destination'] = arrival['destinationName']
            if (result_arrival[line].get('expectedArrivals') == None):
                result_arrival[line]['expectedArrivals'] = []
            result_arrival[line]['expectedArrivals'].append(arrival['expectedArrival'])
            result_arrival[line]['expectedArrivals'].sort()
            result_arrival[line]['towards'] = arrival['towards']

        return result_arrival


    def get_arrivals_for_stop_point(self, stop_point):
        response = requests.get(
            self._url + "/StopPoint/" + stop_point + "/arrivals?app_key=" + self._app_key + "&app_id=" + self._app_id)
        result_arrivals = []
        for api_arrival in response.json():
            is_arrival_in_result = False
            for result_arrival in result_arrivals:
                if (result_arrival['lineId'] == api_arrival['lineId']):
                    arrivalTime = datetime.strptime(api_arrival['expectedArrival'], '%Y-%m-%dT%H:%M:%SZ').strftime('%H:%M')
                    result_arrival['expectedArrivals'].append(arrivalTime)
                    result_arrival['expectedArrivals'].sort()
                    is_arrival_in_result = True

            if (not is_arrival_in_result):
                arrival = {}
                arrival['lineId'] = api_arrival['lineId']
                arrival['lineName'] = api_arrival['lineName']
                arrival['stationName'] = api_arrival['stationName']
                arrival['destinationName'] = api_arrival['destinationName']

                if (arrival.get('expectedArrivals') == None):
                    arrival['expectedArrivals'] = []

                arrivalTime = datetime.strptime(api_arrival['expectedArrival'], '%Y-%m-%dT%H:%M:%SZ').strftime('%H:%M')
                arrival['expectedArrivals'].append(arrivalTime)
                arrival['expectedArrivals'].sort()
                result_arrivals.append(arrival)
        return result_arrivals