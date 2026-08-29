# AWS global infraestructure

* AWS is a collection of smaller groupings of infraestructure connected together by a global high speed network 
* Some services are deployed individually in each region and others act from a global perspective

## AWS Regions

* Is an area of the world and inside is a full deployment of AWS infraestructure
* Benefits:
    * Geographic separation: Isolated Fault Domain
    * Geopolitical separation: Different governance
    * Location control: Performance

## AWS Edge Locations

* Are much smaller than regions
* Generally only have content distribution services and some types of edge computing

## Availability Zone (AZ)

* Isolated Infraestructure inside a region
* Is logical thing inside AWS
* AWS could span services across many AZs to make them resilient

## Service Resilience

* Globally Resilient
    * Services operates globally with a single database, and its data is replicated across multiple regions
* Region Resilient
    * Services which operates in a single region with one set of data per region
* AZ resilient
    * Services that are run from a single AZ
