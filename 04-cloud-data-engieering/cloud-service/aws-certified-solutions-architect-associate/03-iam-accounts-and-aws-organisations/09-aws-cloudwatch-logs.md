# CloudWatch Logs

* Public Service: usable from AWS or on-premises
* It's a regional service
* Store, monitor and access logging data (a piece of information data and a timestamp)
* AWS integrations: EC2, VPC Flow Logs, Lambda, CloudTrail, R53 and more
* Any service which integrate with CloudWatch Logs can store data directly and the security is provided by using IAM roles or service roles
* To integrate external services/apps it's needed to use CloudWatch agent 
* Can generate metrics based on logs, this is known as metric filter

## Architecture

* Logging sources (AWS products and services, external applications, APIs, etc) inject data into CloudWatch logs as Log events
* Log events are composed of a timestamp and a message block and are stored inside Log streams
* Log streams are a sequence of Log events from the same source
* Log groups are containers for multiple Log streams for the same type of logging
    * Store configuration settings, like retention settings and permissions
    * Metric filters are defined here
