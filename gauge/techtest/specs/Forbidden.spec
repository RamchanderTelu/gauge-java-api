Forbidden
=========

tags: forbidden

This spec file details the interaction with the forbidden endpoint and the expected results
of those actions
     
Forbidden is returned when doing a POST to the /forbidden endpoint
------------------------------------------------------------------------------

* Post to the "forbidden" endpoint
* Then the response will be "Forbidden"
* The response code should be "403"

Forbidden is returned when doing a GET to the /forbidden endpoint
----------------------------------------------------------------

* Get to the "forbidden" endpoint
* Then the response will be "Forbidden"
* The response code should be "200"

OK response is returned when doing a GET to /forbidden/last endpoint
-------------------------------------------------------------------------------------------

* Get to the "forbidden/last" endpoint
* Then the response will be "OK"
* The response code should be "200" 
* Retrieve the last updated time from the "forbidden/last" endpoint
* Assert against last updated time "forbidden" endpoint
 

