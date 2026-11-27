# S3 Requester Pays

* Shifts request and data download (transfer) charges from the bucket owner to the AWS account making the request, while the bucket owner continues to pay for object storage
* Authentication required: Anonymous access is not allowed. Requesters must authenticate using an AWS account (IAM user or role)
* Charge acceptance: Requesters must explicitly accept the charges in their request (such as via the x-amz-request-payer header, RequestPayer parameter, or --request-payer CLI flag)
* Bucket-level setting: Configured at the bucket level (BucketOwner is the default; Requester enables it). Doesn't work with static website hosting

## Cost Split

* Requester pays: S3 request fees (such as GET, PUT, POST, LIST) and data download/transfer costs.
* Bucket owner pays: Data storage fees and RestoreObject retrieval charges. Owners also pay for requests returning AccessDenied (403 Forbidden) that originate inside the bucket owner's AWS account or organization.
