# High Availability vs Fault Tolerance vs Disaster Recovery

## High Availability

* Aims to ensure an agreed level of operational performance, usually uptime, for a higher than normal period
* A highly available system is one designed to be online and providing services as often as possible
* A highly available system its designed, so that when it fails its components can be replaced or fixed as quickly as possible, often using automation to bring systems back into service

## Fault Tolerance

* Is the property that enables a system to continue operating properly in the event of the failure of some (one or more faults within) of its components
* First, its needed to minimize outages, and also is needed to design the system to be able to tolerate the failure, which means levels of redundancy and system components

## Disaster recovery

* A set of policies, tools and procedures to enable the recovery or continuation of vital technology infraestructure and systems following a natural or human-induced disaster
* Is about what to plan for and do when disaster occurs
* A good DR plan means taking regular backups
* Key metrics
    * RTO (Recovery Time Objective): How long can your system be offline after a disaster before it causes unacceptable harm? (How fast must you recover?)
    * RPO (Recovery Point Objective): How much data loss can you tolerate? Measured in time (e.g., "we can only afford to lose the last 1 hour of data", which means backups must happen hourly).
* Strategies
    * Backup & Restore: Cheapest, highest RTO/RPO.
    * Pilot Light: Core data is synced, but infrastructure is turned off until needed.
    * Warm Standby: A scaled-down version of your production environment is always running.
    * Multi-Site (Active-Active): Most expensive, near-zero RTO/RPO because traffic is handled by multiple full environments simultaneously.
