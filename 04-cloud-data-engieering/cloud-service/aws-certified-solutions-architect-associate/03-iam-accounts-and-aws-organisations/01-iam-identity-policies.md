# Identity Policies

* IAM policies are a type of policy which get attached to identities (IAM users, IAM groups and IAM roles) inside AWS
* IAM policies deny or allow access to AWS products and features to any identity which uses that policy
* AWS works through all of the statements one by one and reviews any that apply to a particular identity accessing a particular resource in a particular way
* Explicit deny >> Explicit allow >> Default deny (implicit)

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "FullAccess",
            "Effect": "Allow",
            "Action": ["s3:*"],
            "Resource": ["*"]
        },
        {
            "Sid": "DenyCatBucket",
            "Action": ["s3:*"],
            "Effect": "Deny",
            "Resource": ["arn:aws:s3:::catgifs", "arn:aws:s3:::catgifs/*"]
        }
    ]
}
```

## Statements

* Sid: Statement ID, this is an optional field which lets to identify a statement and what it does
* Action: matches one or more actions. It can be very specific and list a specific individual action
* Resources: matches one or more resources. It uses the ARN (Amazon Resource Name)
* Effect: is either "Allow" or "Deny"

## Type of policies

* Inline policies:
    * Written directly into a single IAM user, group or role
    * Strict one-to-one: cannot be shared or attached to multiple identies

* Managed policies:
    * Standalone objects: Independent JSON documents that exist separately from identities
    * Reusable: Can be attached to multiple users, groups, or roles at the same time
    * There are two types:
        * AWS managed policies: Managed by AWS, cannot be edited or deleted
        * Customer managed policies: created inside an AWS account, can be written, edited and version-controled
