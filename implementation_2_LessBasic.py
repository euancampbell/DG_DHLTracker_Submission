import http.client
import urllib.parse
import json
import os

# Import configuration settings from settings.py
from settings import urls, mock_data, production


class DHL:
    """
    A class for interacting with DHL's APIs.
    """

    def __init__(self):
        self.api_key = None
        self.base_url = None

    def call_endpoint(self, endpoint, params):
        """
        Calls the DHL API endpoint.

        Args:
            endpoint (str): The API endpoint to call.
            params (dict): Query parameters for the API request.

        Returns:
            dict: JSON response from the API.
        """
        if not production:
            # Return mock data for testing purposes in a non-production environment
            try:
                return mock_data[endpoint][str(params)]
            except KeyError:
                return {'error': 'mock data not found'}

        params = urllib.parse.urlencode(params)

        # Establish HTTPS connection to the DHL API base URL
        connection = http.client.HTTPSConnection(self.base_url)

        # Set up header
        self.headers = {
            'Accept': 'application/json',
            'DHL-API-Key': self.api_key
        }

        try:
            print(
                f'calling {self.base_url}{endpoint} with parameters {params} and API key {self.api_key}')
            connection.request("GET", endpoint + params, "", self.headers)
        except:
            raise Exception('Connection error')

        response = connection.getresponse()

        data = json.loads(response.read())

        connection.close()

        return data


class ShipmentTrackingUnified(DHL):

    """
    A class for unified shipment tracking using the DHL API.

    This class extends the DHL API functionality to provide shipment tracking services for DHL shipments.

    Attributes:
        api_key (str): The DHL API key required for authentication.
        base_url (str): The base URL for the shipment tracking API.

    """

    def __init__(self):

        self.api_key = os.getenv('stu_api_key', default=None)
        self.base_url = urls['shipment_tracking_unified_base_url']

    def track_shipment(self, tracking_id=None):
        """
        Track a shipment using DHL's Shipment Tracking API.

        Args:
            tracking_id (str): The tracking number of the shipment to track.

        Returns:
            dict: Details of the shipment's tracking information.
        """
        params = {
            'trackingNumber': tracking_id,
            'service': 'express'
        }

        # Call the 'track_shipments' API endpoint
        details = self.call_endpoint(urls['track_shipments'], params)

        return details

    def last_tracking_event(self, tracking_id):
        """
        Get the last tracking event of a shipment.

        Args:
            tracking_id (str): The tracking number of the shipment.

        Returns:
            dict: Details of the last tracking event.
        """
        all_details = self.track_shipment(tracking_id)

        # Retrieve the last tracking event from the shipment's events list
        if 'status' in all_details:
            # Incorrect response received
            return all_details
        else:
            return all_details["shipments"][0]["events"][-1]


class LocationFinderUnified(DHL):
    """
    A class for unified location finder functionality using the DHL API.

    This class extends the DHL API functionality to provide location finder services.

    Attributes:
        api_key (str): The DHL API key required for authentication.
        base_url (str): The base URL for the location finder API.

    """

    def __init__(self):
        """
        Initialize the LocationFinderUnified class.

        It sets the API key and base URL for location finder services.
        """
        self.api_key = os.getenv('lfu_api_key', default=None)
        self.base_url = urls['location_finder_unified_base_url']

    def service_point_locations(self, country_code=None, city=None, radius=5000):
        """
        Retrieve a list of DHL service point locations within a specified radius from a given address.

        Args:
            country_code (str): The two-letter country code where you want to find service point locations.
            city (str): The city or address locality where you want to find service point locations.
            radius (int, optional): The radius (in meters) within which to search for service point locations. Default is 5000 meters.

        Returns:
            dict: A dictionary containing the response data from the DHL API, including information about service point locations.
        """
        params = {
            'countryCode': country_code,
            'addressLocality': city,
            'radius': radius,
            'limit': 2
        }

        # Call the 'track_shipments' API endpoint
        details = self.call_endpoint(urls['location_finder'], params)

        return details


if __name__ == "__main__":

    tracking_event_1 = ShipmentTrackingUnified(
    ).last_tracking_event(tracking_id='7777777770')

    tracking_event_2 = ShipmentTrackingUnified(
    ).last_tracking_event(tracking_id='8264715546')

    service_location_1 = LocationFinderUnified().service_point_locations(country_code='GB',
                                                                         city='London',
                                                                         radius=5000)

    """
    OUTPUTS

    tracking_event_1 (7777777770): {'description': 'Shipment picked up'}
    tracking_event_2 (8264715546): {"title":"No result found","status":404,"detail":"No shipment with given tracking number found."}


    service_location_1: CAMON Geschenkartikel, Nürnberg, Kaiserstr. 15
    """
    if mock_data:
        print('ALERT: MOCK DATA ENABLED\n')

    print('Scenario 1 - tracking 7777777770')
    print(tracking_event_1)

    print('\nScenario 2 - tracking 8264715546')
    print(tracking_event_2)

    print('\nExtra Task - Services locations')
    print(service_location_1)
