# Shared Responsability model

* In each of cloud service models, there were parts of the infraestructure stack that the user is responsible for as the customer and parts of the infraestructure stack that the vendor or provider is responsible for

* AWS is responsible for the security of the cloud, whereas the customer is responsible for the security in the cloud
* AWS is responsible for the securify of
    * Hardware/AWS global infraestructure: AWS regions, the Availability Zones and the edges locations
    * Compute storage databases and networking
    * Any software which assists in those services
* The customer is responsible for:
    * Client-side data encryption, integrity and authentication
    * Server-side encryption (file system and/or data)
    * Networking traffic protection (encryption, integrity, identity)
    * Operating system, network and firewall configuration
    * Applications, identigy and access management to things implemented, managed and controled by the customer
    * Any customer data
