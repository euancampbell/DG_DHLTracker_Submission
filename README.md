# SE Technical Test 2.2 by Euan Campbell

Please find the submission for 'SE Technical Test 2.2'.

Two solutions have been provided, each solving tasks 1 and 2. Below outlines a brief description of the differences and any considerations for future development.

## implementation_1_Basic.py

A bare-bones implementation using a minimal approach with 2 functions, neither of which are dependant on the other. Quick and dirty to create, however loses out on benefits like being easy to make changes, or expansion in the future to further APIs.

## implementation_2_LessBasic.py

Expanded implementation using a class structure for better reusability and maintainability.

A parent DHL class allows for any future DHL API integration to use the same functions, with any changes being made across each API instead of needing to be performed for each one.

## Other

### Configuration
Parameters can come from one of three locations:

- Environment variable (API Keys)
- User input (tracking numer, country, city, radius)
- settings.py (URLs, mock data, production toggle)

### Setup

1) Add the environment variables.
```
> export stu_api_key=<api_key>
> export lfu_api_key=<api_key>
```
2) Update settings.py.
```
production = True
```
3) Run.
```
> python3 implementation_1_Basic.py
> python3 implementation_2_LessBasic.py
```


### Future Changes
A few changes would be recommended for any future implementation.

- **Monitoring and alerting**: Due to time constraints, neither solution provides any monitoring, alerting, or logging.
- **More parameters**: Some endpoints have additional parameters that are not yet supported. Eg, /location-finder/v1/find-by-address allows for searching not just by Country Code and City (addressLocality), but also by postalCode, streetAddress, providerType, locationType, serviceType, and currentDate. The implementation could be expanded to support flexible parameters based on the what the source is looking for.
- **Validation improvements**: All validation is currently put on the DHL API. This provides some benefits, but could be improved to handle errors better for the dependant service.
- **Central service**: Depending on the enterprise architecture, it could be beneficial to build this out into its own internal service for central data access. Additional benefits include, potential cost savings with cache, and easier maintenance if using something similar to a micro service architecture.
- **Better handling of mock data**: Due to the API rate limits, mock data was configured to make implementing the post-API steps. This could be expanded with automatically taking parameters into account instead of being hard-coded.