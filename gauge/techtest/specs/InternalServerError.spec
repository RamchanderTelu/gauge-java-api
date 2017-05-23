

Internal Server Error
==============

tags: internal_server_error

This spec file details the interaction with the internal_server_error endpoint and the expected results
of those actions

Internal Server Error is returned when doing a POST to the /internal_server_error endpoint
------------------------------------------------------------------------------      

* Post to the "internal_server_error" endpoint
* Then the response will be "Internal Server Error"
* The response code should be "500"

Internal Server Error is returned when doing a GET to the /internal_server_error endpoint
----------------------------------------------------------------

* Get to the "gateway_timeout" endpoint
* Then the response will be "Internal Server Error"
* The response code should be "500"

OK of the last response is returned when doing a GET to /internal_server_error/last endpoint
-------------------------------------------------------------------------------------------

* Get to the "forbidden/last" endpoint
* Then the response will be "OK"
* The response code should be "200"
* Retrieve the last updated time from the "internal_server_error/last" endpoint
* Assert against last updated time "internal_server_error" endpoint
 
