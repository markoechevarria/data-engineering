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
* Imposes a 40 KB metadata and index charge per archived object
* Minimum duration charge of 90 days - objects can be stored for less, but the minimum billing always applies
* Objects cannot be mande publicly accessible, any access of data requires a retrieval process
* Data is retrieved to a temporary copy only
    * Expedited: 1-5 minutes
    * Standard: 3-5 hours
    * Bulk: 5-12 hours (free)
* First byte latency of minutes to hours
* Used for long-lived data where frequent or realtime access isn't needed, minutes-hours retrieval

## S3 Glacier Deep Archive

* 99.999_999_999_99% durability
* Replication over 3 AZ's
* Imposes a 40 KB metadata and index charge per archived object
* Minimum duration charge of 180 days - objects can be stored for less, but the minimum billing always applies
* Objects cannot be mande publicly accessible, any access of data requires a retrieval process
* Data is retrieved to a temporary copy only
    * Stanrdar (12 hours)
    * Bulk (up to 48 hours)
* First byte latency of hours or days
* Used for long-lived data that rarely needs to be accesed hours or day for retrieval

## S3 Intelligent-Tiering

* A Storage class which contains five different storage tiers all within
* Objects in this class have a range of ways to be stored
    * Frequent Access: like S3 standard
    * Infrequent Access: like S3 standard infrequent access
    * Archive Instant Access: accesed less frequently, like S3 Glacier instant retrieval
    * Archive Access: like S3 Glacier flexible retrieval
    * Deep Archive: like S3 Glacier Deep archive
* This type of storage choose the type of storage that it uses itself, all from the tiers available within the storage class15
* Monitors and automatically moves any objects not accessed for 30 days to a low cost infrequent access tier and eventually to archive instant access, archive access or deep archive tiers
* Has a monitoring and automation cost per 1,000 objects. The frequent access tier costs the same as S3 standard, the infrequent the same as Standard-IA, Archive Instant, Archive and Deep Archive are comparable to their S3 glacier equivalents
* As objects are accessed, they are moved back to the frequent access tier. There are no retrieval fees for accessing objects
* Should be used for long-lived data with changing or unknown patterns

## S3 Express OneZone

* Similar to S3-Standard
* It differs in:
    * Has "single digit miliseconds" first byte latency and is up to 10x faster than S3 Standard
    * It uses only one AZ
    * Is charged per gigabyte at a more expensive fee than S3-standard, but requesting pricing is around 50% cheaper
* Uses Directory Buckets with Different Naming, Endpoints and a different feature set
* Use for workloads that require consisten, high performance, low latency access
