
production = False

urls = {
    # Shipment Tracking
    'shipment_tracking_unified_base_url': 'api-eu.dhl.com',
    'track_shipments': '/track/shipments?',

    # Location Finder
    'location_finder_unified_base_url': 'api.dhl.com',
    'location_finder': '/location-finder/v1/find-by-address?'
}


# Mock data used to allow for unlimited usage
mock_data = {
    '/track/shipments?': {
        'scenario_1': {'shipments': [{'id': '7777777770', 'service': 'express', 'origin': {'address': {'addressLocality': '-'}, 'servicePoint': {'url': 'http://www.dhl.com/en/country_profile.html', 'label': 'Origin Service Area'}}, 'destination': {'address': {'addressLocality': '-'}, 'servicePoint': {'url': 'http://www.dhl.com/en/country_profile.html', 'label': 'Destination Service Area'}}, 'status': {'timestamp': '2023-10-05T10:13:00', 'location': {'address': {
            'addressLocality': 'NUERNBERG - GERMANY'}}, 'statusCode': 'transit', 'status': 'transit', 'description': 'Arrived at DHL Delivery Facility NUERNBERG - GERMANY'}, 'details': {'proofOfDeliverySignedAvailable': False}, 'events': [{'timestamp': '2023-10-05T10:13:00', 'location': {'address': {'addressLocality': 'NUERNBERG - GERMANY'}}, 'description': 'Arrived at DHL Delivery Facility NUERNBERG - GERMANY'}, {'description': 'Shipment picked up'}]}]},
        'scenario_2': {'title': 'No result found', 'status': 404, 'detail': 'No shipment with given tracking number found.'}
    },
    '/location-finder/v1/find-by-address?': {'locations': [{'url': '/locations/8003-4305585', 'location': {'ids': [{'locationId': '8003-4305585', 'provider': 'parcel'}], 'keyword': 'Postfiliale', 'keywordId': '626', 'type': 'servicepoint'}, 'name': 'CAMON Geschenkartikel', 'distance': 181, 'place': {'address': {'countryCode': 'DE', 'postalCode': '90403', 'addressLocality': 'Nürnberg', 'streetAddress': 'Kaiserstr. 15'}, 'geo': {'latitude': 49.452319, 'longitude': 11.076538}}, 'openingHours': [{'opens': '10:30:00', 'closes': '15:00:00', 'dayOfWeek': 'http://schema.org/Monday'}, {'opens': '15:30:00', 'closes': '19:00:00', 'dayOfWeek': 'http://schema.org/Monday'}, {'opens': '10:30:00', 'closes': '15:00:00', 'dayOfWeek': 'http://schema.org/Tuesday'}, {'opens': '15:30:00', 'closes': '19:00:00', 'dayOfWeek': 'http://schema.org/Tuesday'}, {'opens': '10:30:00', 'closes': '15:00:00', 'dayOfWeek': 'http://schema.org/Wednesday'}, {'opens': '15:30:00', 'closes': '19:00:00', 'dayOfWeek': 'http://schema.org/Wednesday'}, {'opens': '10:30:00', 'closes': '15:00:00', 'dayOfWeek': 'http://schema.org/Thursday'}, {'opens': '15:30:00', 'closes': '19:00:00', 'dayOfWeek': 'http://schema.org/Thursday'}, {'opens': '10:30:00', 'closes': '15:00:00', 'dayOfWeek': 'http://schema.org/Friday'}, {'opens': '15:30:00', 'closes': '19:00:00', 'dayOfWeek': 'http://schema.org/Friday'}, {'opens': '10:30:00', 'closes': '19:30:00', 'dayOfWeek': 'http://schema.org/Saturday'}], 'closurePeriods': [], 'serviceTypes': ['parcel:pick-up', 'parcel:drop-off-unlabeled', 'parcel:drop-off'], 'averageCapacityDayOfWeek': []}, {'url': '/locations/8003-4135939', 'location': {'ids': [{'locationId': '8003-4135939', 'provider': 'parcel'}], 'keyword': 'Postfiliale', 'keywordId': '609', 'type': 'servicepoint'}, 'name': 'American Store & British Empire', 'distance': 507, 'place': {'address': {'countryCode': 'DE', 'postalCode': '90402', 'addressLocality': 'Nürnberg', 'streetAddress': 'Frauengasse 14'}, 'geo': {'latitude': 49.449487, 'longitude': 11.075378}}, 'openingHours': [{'opens': '11:00:00', 'closes': '18:00:00', 'dayOfWeek': 'http://schema.org/Monday'}, {'opens': '11:00:00', 'closes': '18:00:00', 'dayOfWeek': 'http://schema.org/Tuesday'}, {'opens': '11:00:00', 'closes': '18:00:00', 'dayOfWeek': 'http://schema.org/Wednesday'}, {'opens': '11:00:00', 'closes': '19:00:00', 'dayOfWeek': 'http://schema.org/Thursday'}, {'opens': '11:00:00', 'closes': '19:00:00', 'dayOfWeek': 'http://schema.org/Friday'}, {'opens': '10:00:00', 'closes': '19:00:00', 'dayOfWeek': 'http://schema.org/Saturday'}], 'closurePeriods': [], 'serviceTypes': ['parcel:pick-up', 'parcel:drop-off-unlabeled', 'parcel:drop-off'], 'averageCapacityDayOfWeek': []}]}

}
