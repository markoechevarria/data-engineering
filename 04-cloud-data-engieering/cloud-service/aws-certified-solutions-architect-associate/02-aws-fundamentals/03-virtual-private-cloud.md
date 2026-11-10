# Virtual Private Cloud (VPC)

* Service to create private networks inside AWS
* Allows to connect private netoworks to on-premise networks
* Allows to connect to other clouds platforms
* A VPC exists within 1 account and 1 region
* VPCs are regional services, they are region resilient, they operate from multiple AZs within a specific AWS region
* Private and Isolated unless they are decided otherwise
* Default VPC (only one per region) and Custom VPCs (many VPC per region)
* Every VPC is allocated a range of IP addresses called the VPC CIDR
* Custom VPCs can have multiple CIDRs
* For every VPC, we can create subnets (parts of the VPC's CIRD range), and those can be allocated to one and only one availability zone

## Default VPC

* The default VPC only gets one CIDR range => 172.31.0.0/16
* Is preconfigured to have one subnet in every AZ within the AWS region
* There's can be only one or zero default VPC per region, and it can be removed and recreated
* Some services assumes the default VPC will be present
* /20 Subnet in each AZ in the region
* Each default VPC provides a Internet Gateway (IGW), Security Group (SG) and NACL (network ACL)
* By default anything placed in the default VPC subnets is assigned a public IPv4 address
