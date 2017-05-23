GatewayTimeout
==============

tags: gateway_timeout

This spec file details the interaction with the gateway_timeout endpoint and the expected results
of those actions
     
Gateway timeout is returned when doing a POST to the /gateway_timeout endpoint
------------------------------------------------------------------------------

* Post to the "gateway_timeout" endpoint
* Then the response will be "Gateway timeout"
* The response code should be "503"

Gateway timeout is returned when doing a GET to the /gateway_timeout endpoint
----------------------------------------------------------------

* Get to the "gateway_timeout" endpoint
* Then the response will be "Gateway timeout"
* The response code should be "200"

OK of the last response is returned when doing a GET to /gateway_timeout/last endpoint
-------------------------------------------------------------------------------------------

* Get to the "gateway_timeout/last" endpoint
* Then the response will be "OK"
* The response code should be "200"
* The last updated date/time for the latest POST
 
