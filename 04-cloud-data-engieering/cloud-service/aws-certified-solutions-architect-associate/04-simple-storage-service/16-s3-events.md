# S3 Event Notifications

* Notification generated when events occur in a bucket
* Can be delivered to SNS, SQS, Lambda, and EventBridge
* Events:
    * Object Created (Put, Post, Copy, CompleteMultiPartUpload)
    * Object Delete (*, Delete, DeleteMarkerCreated)
    * Object Restore (Post (initiated), Completed, Expired (delete))
    * Replication (OperationMissedThreshold, OperationReplicatedAfterThreshold, OperationNotTracked, OperationFailedReplication)

## Architecture

* Event Notification config: match or look out for specific events that we want to be notified of
* Events interact with other services
* Events that are actually generated and being sent onwards are JSON objects
