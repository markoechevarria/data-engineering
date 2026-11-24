# S3 Lifecycle Configuration

* A lifecycle configuration is a set of rules which are applied to a bucket
* Rules consists of actions which are going to apply based on some criteria. They are not based on access
* Rules can apply to a whole bucket or groups of objects (defined by the prefix and tags)
* Actions are of two types
* Transition actions: change the storage class of whatever is being affected
* Expiration actions: delete whatever is affected

## Lifecycle transition

* Can be thought of as a waterfall
    1. S3 Standard -> S3 Standard IA -> S3 Intelligent Tiering -> One Zone IA -> S3 Glacier Instant Retrieval -> S3 Glacier Flexible Retrieval -> Glacier Deep Archive
    * Transitions flows downward on the waterfall
    * S3 One Zone IA cannot fall into S3 Glacier Instant Retrieval

## Considerations

* Transitions can't happend in an upward direction
* Objects smallers than 128kb cannot be transitioned by default. Small objectts may cost more due to minimum size billing
* Minimum of 30 days in S3 before transition Standard IA or One Zone-IA
* A single rule cannot transition to Standard-IA or One Zone-IA and then to glacier classes within 30 days (duration minimum)
* A single rula cannot transition to Glacier Instant Retrieval and then to Glacier Flexible Retrieval within 90 days (duration minimum)
