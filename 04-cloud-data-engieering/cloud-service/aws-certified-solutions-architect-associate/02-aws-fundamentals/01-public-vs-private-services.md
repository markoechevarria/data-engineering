# Public vs Private services

* Aws services can be categorized (based on networking only) into two main types
    * A public service is something which is accessed using public endpoints
    * A private service is something which runs withing a VPC (Virtual Private Cloud)
* Both types of services have permissions and networking

## "Public Internet" zone

* Where internet-based services operate

## AWS private zone

* VPC (Virtual Private Cloud) are AWS private zones which are isolated (VPCs can't communicate with each other)
* Nnothing from the internet can reach them (unless the owner configured it)
* Private networks can be connected together 

## AWS public zone

* Runs between the "public internet" zone and the AWS private zone networks
* This is not on the public internet, it's a network which is connected to the public internet
* This is where service with public endpoints live
* To access AWS public services from anywhere with a "public internet" connection, the communication uses the "public internet" for transit to and from the AWS public zone

* An internet gateway can be attached to a VPC
