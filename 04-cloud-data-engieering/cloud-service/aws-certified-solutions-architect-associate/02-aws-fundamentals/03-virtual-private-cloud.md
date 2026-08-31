# Virtual Private Cloud (VPC)

* Service to create private networks inside AWS
* Allows to connect private services to on-premise networks
* Allows to connect to other clouds platforms

* A VPC exists within 1 account and 1 region
* Private and Isolated unless they are decided otherwise
* Default VPC (only one per region) and Custom VPCs (many VPC per region)
    * Custom VPCs are used in all serious AWS deployments

## Default VPC

* Every VPC is allocated a range of IP addresses called the VPC CIDR
* The default VPC only gets one CIDR range => 172.31.0.0/16
* The default VPC is subdivided into subnets (part of the VPC's CIDR range), each subnet is located in one availability zone within the AWS region

* There's can be only one or zero default VPC per region, and it can be removed and recreated
* Some services assumes the default VPC will be present
* /20 Subnet in each AZ in the region
* Each default VPC provides a Internet Gateway (IGW), Security Group (SG) and NACL (network ACL)
* By default anything placed in the default VPC subnets is assigned a public IP version four address
