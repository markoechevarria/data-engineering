# Route53

* It's a global service, globally resiient with a single (replicated) database 

## Allow register domains

* Registries
    * Are the companies which manage the top level domains. 
    * They have been delegated this ability by IANA who manage the root zone for DNS
    * Each registry manage one specific zone
* When a domain is registered
    * Route 53 checks with the registry for that top level domain if the domain is available
    * Route 53 creates a zone file (a database which contains all of the DNS information for a particular domain) for the domain being registered
    * Route 53 allocates name services for this zone. Services which Route 53 creates and manages which are distributed globally. There are generally four for one individual zone
    * Route 53 takes the zone file (known as a hosted zone) and put it onto the name servers
    * Route 53 communicates with the registry and adds these name server records into the zone file for the top level domain

## Host zone files 

* DNS as a service
* Manage zone files (hosted zones) which are hosted on AWS managed name servers (four per zone)
* Can be public, the data is accessed from the internet
* Can be private, it is linked to one or more VPCs and only accessible from within those VPCs
* A hosted zone hosts DNS records

## DNS record types

* NS: (name server) Allow delegation to occur in DNS. Defines which name servers are authorized and authoritative for the hosted zone
* A: maps a host onto an IP version four address
* AAAA: maps a host onto an IP version six address
* CNAME: (canonical name) maps one domain name to another domain name. Cannot point directly at an IP address. Cannot be used at the root domain or zone apex
* Alias: lets map a root domain (or any subdomain) directly to AWS resources. Are free, work at the root apex
* MX: Have two main parts, a priorit and a value. Configure mail exchange servers to handle email delivery and routing for a domain
* TXT: Allows add arbitrary text to a domain. They are used to prove ownership and for domain verification
* DNS TTL: It's a numeric value in seconds. Indicates how longer records can be cached for, what ammount of type is appropiate. TTL are normally mandatories, but can be ignored
