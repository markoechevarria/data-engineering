# Route53

* Allows register domains
* Can host zone files on manage name serves
* It's a global service with a single database
* Is globally resilient

## Allow register domains

* Registries
    * Are the companies which manage the top level domains. 
    * They have been delegated this ability by IANA who manage the root zone for DNS
    * Each registry manage one specific zone
* When a domain is registered
    * Route 53 checks with the registry for that top level domain if the domain is available
    * Route 53 creates a zone file (a database which contains all of the DNS information for a particular domain) for the domain being registered
    * Route 53 allocates name service for this zone. Serves which Route 53 creates and manages which are distributed globally and there are generally four for one individual zone
    * Route 53 takes the zone file (known as a hosted zone) and put it onto the name servers
    * Route 53 communicates with the registry and adds these name server records into the zone file for the top level domain

## Hosted zones

* DNS as a service
* Manage zone files
* A number of servers are allocated and linked to that hosted zone
* Can be public, the data is accessed from the internet
* Can be private, it is linked to one or more VPCs and only accessible from within those VPCs

## DNS record types

### Nameserver records or NS records

* These allow delegation to occur in DNS

### A and AAAA records

* A: maps a host onto an IP version four address
* AAAA: maps a host onto an IP version six address

### CNAME (Canonical Name)

* For a given zone it lets create the equivalent of DNS shortcuts, so host to host records
* They are used to reduce admin overhead
* CNAME cannot point directly at an IP address, only other names

### MX

* MX records have two main parts, a priotity and a value
* Is how a server can find the mail server for a specific domain

### TX

* Allows add arbitrary text to a domain
* They are used to prove ownership

## DNS TTL

* It's a numeric value in seconds
* Indicates how longer records can be cached for, what ammount of type is appropiate
* TTL are normally mandatories, but can be ignored




