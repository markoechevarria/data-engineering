# S3 Bucket Keys (for SSE-KMS)

## Traditional SSE-KMS Architecture

* Every single time an object is uploaded or downloaded, S3 must make a direct PI call to AWS KMS to generate or decrypt a unique Data Encryption Key
* AWS KMS charges a flat fee per API request. If an application processes tens of thousands of objects per second, the KMS API costs can quickly skyrocket
* AWS KMS has strict, region-specific service quotas on transactions per second. High volume S3 workloads writing or reading millions of objects rapidly could easily saturate these KMS limits, causing HTTP 503 throttling errors and failed uploads/downloads

## How S3 Bucket Keys Works

1. When S3 Bucket Keys are enabled and an object is uploaded, S3 requests a special master-level Bucket Key from AWS KMS using a Customer Managed Key (CMK) or AWS managed key
2. Instead of discarding this key inmediately, S3 caches and reuses this bucket-level key locally within the S3 infraestructure for a time-limited period
3. For subsequent object uploads and downloads wihin that timeframe, S3 uses the cached Bucket Key locally to derive/generate unique per-object Data Keys
4. Instead of making a distinct KMS API call per object, S3 only needs to call KMS once periodically to establish a bucket key. This reduces KMS request traffic and associated costs by up to 99%

## Considerations

* Without S3 Buckets Keys, the AWS KMS encryption context uses the individual object ARN; with S3 Bucket Keys enabled, the encryption context shifts to the bucket ARN. If the KMS key policies rely on object-level ARNs you must update those policies to reference the bucket ARN before enabling S3 Bucket Keys, or access will be denied
* Because S3 makes fewer calls to AWS KMS, AWS CloudTrail logs will record fewer KMS events. CloudTril will log the bucket ARN instead of individual objects ARNs for those cryptographic events
* Enabling S3 Bucket Keys on an existing bucket only applies to newly uploaded objects. Existing objects will retain their original object-level KMS mapping unless rewritten/re-uploaded
* If we replicate encrypted objects to a destination bucket, note that ETags may change depending on whether the destination bucket utilizes bucket keys, which can affect applications tightly coupled to ETag validation
