BadRequest
==========

tags: bad_request

This spec file details the interaction with the bad_request endpoint and the expected results
of those actions
     
Bad Request is returned when doing a POST to the /bad_request endpoint
----------------------------------------------------------------------

* Post to the "bad_request" endpoint
* Then the response will be "Bad Request"
* The response code should be "400"

Bad Request is returned when doing a GET to the /bad_request endpoint
------------------------------------------------------------

* Get to the "bad_request" endpoint
* Then the response will be "Bad Request"
* The response code should be "400"

OK is returned when doing a GET to /bad_request/last endpoint
---------------------------------------------------------------------------------------

* Get to the "bad_request/last" endpoint 
* Then the response will be "OK"
* The response code should be "200"
* The last updated date/time for the latest POST
 
