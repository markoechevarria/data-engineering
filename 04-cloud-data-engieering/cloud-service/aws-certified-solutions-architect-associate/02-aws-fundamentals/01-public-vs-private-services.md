# Public vs Private services

* Aws services can be categorized into two main types, public services and private services

* A public service is something which is accessed using public endpoints
* A private AWS service is something which runs withing a VPC (Virtual Private Cloud)

* Both types of services have persmission and networking

## AWS private zone

* VPC (Virtual Private Cloud) are AWS private zones which are isolated (VPCs can't communicate with each other) and nothing from the internet can reach them (unless the owner configured it)

## AWS public zone

* Runs between the public internet and the AWS private zone networks
* This is not on the public internet, it's a network which is connected to the public internet
* This is where service with public endpoints live

* To access AWS public services from anywhere with a public internet connection, the communication uses the public internet for transit to and from the AWS public zone

* Private networks can be connected together 
* An internet gateway can be attached to a VPC
