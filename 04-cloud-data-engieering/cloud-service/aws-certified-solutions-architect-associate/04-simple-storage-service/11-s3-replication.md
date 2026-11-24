# S3 Replication

* Feature that allows configure the replication of objects between a source and destination S3 bucket
* Can be configured within the same or different AWS account

* The source bucket is where the replication configuration is set, which defines the destination bucket and an IAM role
    * The IAM role is configured to allow the S3 service to assume it, it gives permissions to read object on the source bucket, and the permissions required to replicate objects to the destination bucket
* The replication configuration

### Cross Region Replication (CRR)

* Allows the replication of objects from a source bucket to one or more destination buckets in different AWS regions
* It's needed to add a bucket policy on the destination bucket which allows the role from the source account to replicate objects into it

### Same Region Replication (SRR)

* Allows the replication of objects from a source bucket to one or more destination buckets in the same AWS region

## Replication options

* All objects or a subest: Replicate an entire source bucket and that would be all objects, all prefixes, and all tags. Also can be a subset of objects
* Storage class: default is to maintain the same class
* Ownership: default is the source account
* Replication Time Control (RTC): feature which add a guaranteed 15 minute replication SLA onto the process

## Considerations

* By default, replication is not retroactive and versioning needs to be on
* Batch replication can be used to replicate existing objects
* One-way replication: objects are replicated from the source to the destination. There's exists a option which allows bidirectional, and that requres extra configuration
* Replication is capable of handling objects which are unencrypted and encrypted (SSE-S3, SSE-KMS DSSE-KM, SSE-C)
* Source bucket owner needs permissions to objects
* No replicate system events (such as lifecycle management), Glacier or Glacier Deep Archive
* Deletes are not replicated between buckets, but can be added using DeleteMarkerReplication

## Scenarios

* SRR can be used for log aggregation
* SRR can be used to configure some sort of synchronization between different environments
* SRR can be used to implement resilience with strict sovereignty
* CRR can be used for implement global resilience 
* CRR can be used for latency reduction
