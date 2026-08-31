# Elastic Compute Cloud (EC2)

* IAAS: Infraestructure as a Service
* Provides access to virtual machines known as EC2 instances
* Is a private service by-default 
* Uses VPC networking
* EC2 is AZ resilient
* Different instance sizes and capabilities
* Local on-host storage (EC2 Instance Store) or Elastic Block Store (EBS)
* Resources:
    * CPU: determines how much processing can be achieved
    * Memory: fast are to store data that's currently being worked on by the instance
    * Disk: where medium-term data is stored
    * Networking: how the instances communicate with other entities

## Instance Lifecycle

* Running:
    * Can be moved to stopped when it's shut down
    * Can be terminated
    * The 4 resouces are being used and charged
* Stopped
    * Can be moved to running when it's start up
    * Can be terminated
    * CPU, Memory and Networking aren't being used, but Disk are still allocated and charged
* Terminated
    * It deletes the Disk and stop the CPU, Memory and Networking, so any resources is charged
    * It's not reversible

## Amazon Machine Image (AMI)

* Is an image of an EC2 instance
* An AMI can be used to create an EC2 instance or an AMI can be created from an EC2 instance
* AMI components:
    * Permissions: 
        * Public: everyone allowed
        * Owner: Implicit allow
        * Explicit: specific AWS accounts allowed
    * Root Volume: 
        * The drive that boots the operating system
        * Can contains other volumes, extra drives 
    * Block device mapping:
        * Links the volumes that the AMI has, and how they are presented to the Operating System
        * It determines which volume is the boot volume and which volume is a data volume

## Operating systems

* EC2 can run differente operating systems
* To connect to Windows intances, the RDP is used via the port 3389
* To connect to Linux instances, the ssh protocol is used via port 22
