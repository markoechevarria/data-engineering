# Cross-Origin Resource Sharing (CORS)

## Same-Origin Request

* The browser defines an origin (URL, protocol, host and port)
* The browser sends the HTTP request directly
* The server returns the response, and the browser lets the page read it

## Cross-Origin Request

* The browser attaches an "Origin" header showing the current page's scheme, host and port
* The target server checks the "Origin" header against its allowed origins
* If permitted, the server sends back Access-Control-Allow-Origin matching the origin (or * for public access)
*  If the header matches and allows access, the browser exposes the response to client code; otherwise, it blocks access and logs a CORS error

## CORS configuration

* Can be defines using JSON or XML
* Is processed in order, the first rule which matches is used

## Considerations

* Simple requests: directly access a different origin using cross-origin request
* Preflighted requests: a check which the ser will do in advance to the other origin. The browser is first going to send a HTTP request to the other origin to determine if the request is safe to send
* Response header: Access-Control-Allow-Origin, this either contain a wildcard or a particular origin which is allows to make requests
* Response header: Access-Control-Max-Age, indicates how long the results of preflight request can be cached
* Response header: Access-Control-Allow-Methods, is either a wildcard or a list of methods that can be used for Cross-Origin requests (PUT, GET, DELETE, etc)
* Response header: Access-Control-Allow-Headers, the response to a preflight test, is used to indicate which HTTP headers can be used within the actual request
