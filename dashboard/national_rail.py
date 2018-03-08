from zeep import Client
from zeep import xsd
from zeep.cache import SqliteCache
from zeep.transports import Transport

class national_rail:

    def __init__(self, wsdl, token, timeout = 5):
        header = xsd.Element(
            '{http://thalesgroup.com/RTTI/2013-11-28/Token/types}AccessToken',
            xsd.ComplexType([
                xsd.Element(
                    'TokenValue',
                    xsd.String()
                )
            ])
        )

        # I dont need 'header_value' to declare as class variables?
        # WHere the hell this 'header' function is comming from???
        self.header_value = header(TokenValue=token)

        transport = Transport(cache=SqliteCache())
        self.client = Client(
            wsdl=wsdl,
            service_name='ldb',
            port_name='LDBServiceSoap12',
            transport=transport,
            strict=False
    )

    def get_departure_board(self, crs, rows=10, filter_crs=None, filter_type='to', offset=0, window=120):
        response = self.client.service.GetDepartureBoard(rows, crs, filter_crs, filter_type, offset, window, _soapheaders=[self.header_value])
        train_departures = {}
        train_departures['location'] = getattr(response, 'locationName')
        train_departures['destinations'] = []
        departures = getattr(response, 'trainServices')['service']
        for departure in departures:
            location_name = departure['destination']['location'][0]['locationName']
            current_departure = {}
            current_departure['std'] = departure['std']
            if (departure['etd'] != 'On time'):
                current_departure['etd'] = departure['etd']
            current_departure['platform'] = departure['platform']
            is_found_destination = False
            for destination in train_departures['destinations']:
                if (destination['name'] == location_name):
                    destination['departures'].append(current_departure)
                    is_found_destination = True

            if (not is_found_destination):
                dep = {}
                dep['name'] = location_name
                dep['departures'] = []
                dep['departures'].append(current_departure)
                train_departures['destinations'].append(dep)

        return train_departures

    def limit_departure_count(self, departures, count):
        for destination in departures['destinations']:
            destination['departures'] = destination['departures'][0:8]

        return departures
