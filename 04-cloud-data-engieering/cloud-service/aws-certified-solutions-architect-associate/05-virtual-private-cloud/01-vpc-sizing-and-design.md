# VPC Sizing and Design

## Key Considerations

* Configure the VPC CIDR (IPv4 range) and plan for IPV6 if needed
* **VPC Size**: Determines total IP capacity and how many workloads, ENIs, load balancers, and NAT gateways fit
* **Non-overlapping networks**: Connected networks (other VPCs, on-premises, VPN/Direct Connect, partners/vendors) must not use overlapping CIDRs
* **Future growth:** Networks evolve over time—plan capacity before building, while noting AWS allows secondary IPv4 CIDR blocks (up to 5 total per VPC).
* **VPC structure:** Design consistent subnet tiers (public, private, isolated) across multiple Availability Zones (AZs) for high availability.

* VPC Structure - Tiers and Resiliency (Availability) Zones

## Design Considerations

* IPv4 VPC CIDR sizes range from **/28** (16 IPs, smallest) to **/16** (65,536 IPs, largest)
* Preference for RFC 1918 `10.x.x.x` space.
* Avoid common/default ranges (such as `10.0.0.0/16`, `10.1.0.0/16`, and `172.31.0.0/16`) to reduce future collision risk.
* Reserve 2+ CIDR blocks per Region per account (or manage centrally via AWS IPAM).
* Rough IP demand guide: `(Number of Regions) * (Ranges per Region) * (Number of Accounts)`.
* Remember AWS reserves **5 IPs per subnet** (network, VPC router, DNS, future use, and broadcast)

## AWS Sizing Guidance

* Reference VPC sizes: **micro** (`/24`), **small** (`/21`), **medium** (`/19`), **large** (`/18`), **extra large** (`/16`).
* Equal-sized subnets formula: $\text{Subnets per VPC} = 2^{(\text{Subnet Mask} - \text{VPC Mask})}$
* Sizing questions to answer upfront: How many subnets do you need across AZs? How many total IPs? How many usable IPs per subnet (after 5 reserved IPs)?
