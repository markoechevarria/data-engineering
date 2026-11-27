# S3 Inventory

* An automatic way that we can go and get all of the information about objects in a bucket
* Reports an inventory of objects inside a bucket (plus optional fields)
* Encryption, Size, Storage class, Replication status, Object Lock
* Generated daily or weekly (cannot be forced)
* It's needed to wait up to 48 hours for the first report to come through
* Report format - CSV, ORC, parquet
* Multiple inventories can be setup for a single bucket
* Save to target bucket (same/different account, must be same region)
* Needs a bucket policy (S3 access to target bucket)
