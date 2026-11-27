# S3 Access Points

* Helps to improve the manageability of S3 buckets, especially when those buckets are being used by many different teams or users or when buckets store objects with a wide range of functions
* Helps by giving unique entry points into a single S3 bucket, and allowing to have unique access controls on it
* Each with different policies and with different network access controls
* Created via Console or CLI or API
* Each Access Point has a unique DNS address for network access
* Each Access Point has its own policies (equivalent to a bucket policy)
* Access points can be set to only allow a VPC origin. This will need a VPC endpoint in the VPC
* Any permissions defined on an access point need to be also defined on the bucket policy for the parent bucket
* Delegation: on the bucket policy, we grant wide open acccess via the access point
* Access points support cross account access
