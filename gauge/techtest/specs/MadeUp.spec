MadeUp
======

tags: made_up

This spec file details the interaction with the made_up endpoint and the expected results
of those actions
     
Not Found is returned when doing a POST to the /made_up endpoint
----------------------------------------------------------------------

* Post to the "made_up" endpoint
* Then the response will be "Not Found"
* The response code should be "404"

Not Found is returned when doing a GET to the /made_up endpoint
------------------------------------------------------------

* Get to the "made_up" endpoint
* Then the response will be "Not Found"
* The response code should be "404"

Not Found is returned when doing a GET to /made_up/last endpoint
---------------------------------------------------------------------------------------

* Get to the "made_up/last" endpoint 
* Then the response will be "Not Found"
* The response code should be "404"

Not Found is returned when doing a POST to /made_up/last endpoint
---------------------------------------------------------------------------------------

* Get to the "made_up/last" endpoint 
* Then the response will be "OK"
* The response code should be "200"
* Retrieve the last updated time from the "made_up/last" endpoint
* Assert against last updated time "made_up" endpoint
 
