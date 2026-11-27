# S3 Object Lock

* Enforces a write-once-read-many (WORM) model on S3 buckets to block object deletion and overwriting for a set time or indefinitely
* Requires versioning
* Modes of locking:
    * Retention Period: 
    * Legal Hold: 
    * An object version can technically have both of these enabled
* A bucket can have default Object Lock settings (Retention period only)
* Permissions the identity need to have to enable: s3:PutObjectRetention, s3:PutObjectLegalHold

## Retention period

* We need to specify a retention period in days or years
* Bucket default
* The clock starts ticking from when the object version is created, not from when the buckets settings are configured
* Compliance: An object version can't be adjusted, deleted, overwritten for the duration of the retention period. And the retention period itself cannot be changed, event by the account root user until retention expires
* Governance: An object version can't be modified, deleted or overwritten for the duration of the retention period. Special permissions to allow the configuration to be changed can be granted with s3:BypassGovernanceRetention (with special header x-amz-bypass-governance-retention:true)

## Legal Hold

* Set on an object version - ON or OFF
* No retention
* When on we can't delete or override that specific object version
* s3:PutObjectLegalHold is required to add or remove
* Prevent accidental deletion of critical object versions
