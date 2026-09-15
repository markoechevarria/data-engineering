# Identity Policies

* IAM policies are a type of policy which get attached to identities (IAM users, IAM groups and IAM roles) inside AWS
* IAM policies deny or allow access to AWS products and features to any identity which uses that policy

* When an identity attempts to access AWS resources that identity needs to prove who it is to AWS
* AWS knows which policies an identity has and has a list of all statements which apply to a given identity
* AWS works through all of the statements one by one and it reviews any that apply to a particular identity accessing a particular resource in a particular way

## Statements

* Sid: Statement ID, this is an optional field which lets to identify a statement and what it does
* Action: matches one or more actions. It can be very specific and list a specific individual action
* Resources: matches one or more resources. It uses the ARN (Amazon Resource Name)
* Effect: is either "Allow" or "Deny"

## Effect Priorities

* Explicit deny: have the first priority
* Explicit allow: have the second priority
* Default deny (implicit): last priority

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
