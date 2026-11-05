# AWS global infraestructure

* AWS is a collection of smaller groupings of infraestructure connected together by a global high speed network
* Some services are deployed individually in each region and others act from a global perspective

## AWS Regions

* Is a separate geographical area containing multiple Availability Zones
* It does not necessarily contain every AWS service or the entirety of AWS infrastructure
* Benefits:
    * Geographic separation: Regions are isolated from failures affecting other Regions
    * Geopolitical separation: Helps satisfy regulatory, legal, and data residency requirements
    * Location control: Lets you deploy resources closer to users, reducing latency

## AWS Edge Locations

* Are much smaller than regions
* Generally only have content distribution services and some types of edge computing
* They are located in many more places than regions

## Availability Zone (AZ)

* Isolated Infraestructure inside a region
* Is not merely a logical concept. It represents one or more discrete data centers with independent power, networking, and connectivity
* AWS could span services across many AZs to make them resilient

## Service Resilience

* Globally Resilient
    * Services with a global control plane or global endpoint
    * They may operate across multiple Regions or provide globally distributed infraestructure
    * Their data replication and availability models depend on the specific service
* Region Resilient
    * Services whose resources are managed within a particular Region
    * Their resources and data are generally isolated from other Regions unless you explicitly configure cross-Region replication or another resilience mechanism
* AZ resilient
    * Resources deployed in a single AZ are AZ-Scoped
    * An application deployed across multiple AZs can be AZ-resilient if it is designed to continue operating when one AZ fails

