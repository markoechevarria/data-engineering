# Layer 3: Network

* The protocol which can spam multiple different layer 2 networks
* Internet Protocol (IP), it is used to send requests from a network across the internet to one server, and back again
* Routers:
    * Devices, remove frame encapsulation and add new frame encapsulation at every hop

* Packets: Are similar to frames, the difference is that the destination and source addresses could be on opposite sides of the planet
    * Some important fields
        * Source IP Adress
        * Destination IP Adress
        * Protocol (ICMP, TPC, UDP)
        * Data
        * Time to Live (TTL): defines how many hops the packet can move through
    * v6 has both source and destination IP address fields biggers thatn v4

## IP Adressing (v4)

* Dotted decimal notation: 0.0.0.0 - 255.255.255.255
    * Network part: states which IP network this IP address belongs to
    * Host part: represents hosts on that network
    * If the network part of the IP address matches between two different IP addresses, then they are on the same IP network
    * The prefix (/x), indicates that x bits of the IP are the network and the remaining bits are for hosts
* IP address on network are either statically assigned by humans (static IP) or automatically by machines 

## Subnet Mask

* 
