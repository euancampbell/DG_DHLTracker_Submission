import os
import http.client
import json

from settings import urls


def last_tracking_event(tracking_number=None, api_key=None):
    """
    Retrieve the last tracking event for a package using its tracking number.

    Args:
        tracking_number (str): The tracking number of the package for which you want to retrieve tracking information.
        api_key (str): The DHL API key required for authentication.

    Returns:
        dict: A dictionary containing the last tracking event for the specified package.

    Example:
        tracking_event = last_tracking_event(tracking_number='7777777770', api_key='your_api_key')
    """

    conn = http.client.HTTPSConnection(
        urls['shipment_tracking_unified_base_url'])

    headers = {
        'Accept': 'application/json',
        'DHL-API-Key': api_key
    }

    conn.request(
        "GET", f"{urls['track_shipments']}trackingNumber={tracking_number}", headers=headers)

    response = conn.getresponse()
    data = json.loads(response.read())

    try:
        # Extract the last tracking event from the API response.
        last_event = data["shipments"][0]["events"][-1]
    except:
        # If no events are found, set the last event as the entire response.
        last_event = data

    return last_event


def service_point_locations(api_key=None, country_code=None, city=None, radius=5000):
    """
    Retrieve a list of DHL service point locations within a specified radius from a given address.

    Args:
        api_key (str): The DHL API key required for authentication.
        country_code (str): The two-letter country code where you want to find service point locations.
        city (str): The city or address locality where you want to find service point locations.
        radius (int, optional): The radius (in meters) within which to search for service point locations. Default is 5000 meters.

    Returns:
        dict: A dictionary containing the response data from the DHL API, including information about service point locations.

    Example:
        service_location = service_point_locations(api_key='your_api_key', country_code='DE', city='NUERNBERG', radius=4000)
    """
    conn = http.client.HTTPSConnection(
        urls['location_finder_unified_base_url'])

    headers = {'DHL-API-Key': api_key}

    conn.request(
        "GET", f"{urls['location_finder']}countryCode={country_code}&addressLocality={city}&radius={radius}&limit=2", headers=headers)

    response = conn.getresponse()
    data = json.loads(response.read())

    return data


# Task 1 - Develop a function that will return the tracking information of a package by a tracking number
tracking_event_1 = last_tracking_event(
    tracking_number='7777777770', api_key=os.getenv('stu_api_key', default=None))
tracking_event_2 = last_tracking_event(
    tracking_number='8264715546', api_key=os.getenv('stu_api_key', default=None))

# Task 2 - Implement a function to get and return the list of all DHL service point locations within the specified radius from the given address.
service_location_1 = service_point_locations(
    api_key=os.getenv('lfu', default=None), country_code='DE', city='NUERNBERG', radius=4000)

"""
OUTPUTS

tracking_event_1 (7777777770): {'description': 'Shipment picked up'}
tracking_event_2 (8264715546): {"title":"No result found","status":404,"detail":"No shipment with given tracking number found."}


service_location_1: CAMON Geschenkartikel, Nürnberg, Kaiserstr. 15
"""
print(tracking_event_1)
print(tracking_event_2)
print(service_location_1)
