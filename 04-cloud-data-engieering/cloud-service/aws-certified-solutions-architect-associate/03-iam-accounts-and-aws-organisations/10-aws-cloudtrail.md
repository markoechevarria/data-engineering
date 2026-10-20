# AWS CloudTrail

* A product which logs API actions which affect AWS accounts
* Logs API call/activities as a CloudTrail Event (a record of an activity in an AWS account)
* By default stores the last 90 day (free) of CloudTrail Events in the CloudTrail Event History (enabled by default - without any storage service)
* CloudTrail Event types:
    * Management Events: provide information about management operations that are performed on resources inside the AWS account (control plane operation)
    * Data Events: contain information about resource operations performed on or in a resource (it isn't stored by default)
    * Insight Events
* CloudTrail Trail
    * Is the unit of configuration within the CloudTrail product
    * Is how S3 and CWLogs are configured
    * It's neccesary to create one or more Trails to customize the CloudTrail service
* CloudTrail is a regional service, but can be configured to work on two ways
    * One-region trail: logs evenst for the region that it's created in
    * All regions: a collection of trails in every AWS region, but managed as one logical trail
* Some services log events globally to one region (global service - IAM, STS, CloudFront) and a trail needs to be enabled in order to log those events
* A trail can store the events in a definable s3 bucket (that events can be stored indefinitely and only the s3 use will be charged)
* Logs are stored as a set of compressed JSON log files
* Cloudtrail can be integrated with CloudWatch logs and the data can be stored in that product
* It's not realtime: there is a delay of roughly 15 minutes

* Organizational CloudTrail Trail
    * Can be created from the management account of an organization
    * Store all information for all of the accounts inside the organization
