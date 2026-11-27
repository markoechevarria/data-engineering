# S3 Access Logs

* Provide detailed records of the requests made to a specific S3 bucket, helping you audit security, troubleshoot errors, and analyze traffic patterns
* Destination bucket (same region and account)
* Access Logging can be enabled via the console UI or via PUT Bucket Logging
* Logging is managed by S3 Log Delivery Group, which has a service principle of logging.s3.amazonaws.com. This system reads the logging configuration that we set on the source bucket. We need to give access this service to the destination bucket and it's done with the bucket policy on the destination bucket
* Best Efforts log delivery, accesses to source bucket are usually logged in Destination Bucket within a few hours
* Log files consist of Log Records:
    * Records are newline-delimited
    * Attributes are space-delimited

## Considerations

* Log file includes a number of different lines for the access, and within that, there are going to be attributes which tell about the S3 access
* Each record includes: requester, operation, HTTP status, error code, bytes sent, timestamps and more
* One destination bucket for multiple source buckets (use prefixes)
* Useful for security audits, usage patterns and costs
* Log lifecycle is managed by the user, it's recommended to use S3 lifecycle policies
