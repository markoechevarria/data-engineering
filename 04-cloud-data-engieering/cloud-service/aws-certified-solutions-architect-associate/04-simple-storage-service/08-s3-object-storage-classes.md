# S3 Object Storage Classes

## S3 Standard

* It's the default
* 99.999_999_999_99% durability
* Replication over 3 AZ's and Content-MD5 Checksums and Cyclic Redundancy Checks (CRCs) are used to detect and fix any data corruption
* Billed a GB/m fee for data stored. 
* No specific retrieval fee, no minimum duration, no minimum size
* Miliseconds first byte latency and objects can be made publicly available
* Used for Frequently Accessed Data which is important and Non Replaceable

## S3 Standard IA

* 99.999_999_999_99% durability
* Replication over 3 AZ's
* Almost half of the S3 Standard GB/m fee for data stored
* Retrieval fee of per GB data
* Minimun duration charge of 30 days - objects can be stored for less, but the minimum billing always applies
* Minimum capacity charge of 128KB per object
* Used for long-lived data, important or irreplaceable, but where the data is accesed Infrequently

## S3 One Zone-IA

* 99.999_999_999_99% durability
* There's no replication, only one AZ is used
* Much cheaper than S3 Standard and S3 Standard IA
* Retrieval fee of per GB data
* Minimun duration charge of 30 days - objects can be stored for less, but the minimum billing always applies
* Minimum capacity charge of 128KB per object
* Used for long-lived data which is non-critical and replaceable and where access is infrequently

## S3 Glacier Instant

* 99.999_999_999_99% durability
* Replication over 3 AZ's
* Retrieval fee of per GB data
* Minimum capacity charge of 128KB per object
* Minimum duration charge of 90 days - objects can be stored for less, but the minimum billing always applies
* Storage cost are cheaper
* Used for long-lived data accessed once per quarter with milisecond access

## S3 Glacier Flexible Retrieval

* 99.999_999_999_99% durability
* Replication over 3 AZ's
* Billed about one-sixth of the S3 Standard GB/m fee for data stored. 
* Retrieval fee of per GB data
* Minimum capacity charge of 128KB per object

* Objects cannot be mande publicly accessible, any access of data requires a retrieval process
* First byte latency of minutes to hours
* Data is retrieved to a temporary copy only
    * Expedited: 1-5 minutes
    * Standard: 3-5 hours
    * Bulk: 5-12 hours (free)

* Minimum duration charge of 90 days - objects can be stored for less, but the minimum billing always applies
* Storage cost are cheaper
* Used for long-lived data accessed once per quarter with milisecond access
