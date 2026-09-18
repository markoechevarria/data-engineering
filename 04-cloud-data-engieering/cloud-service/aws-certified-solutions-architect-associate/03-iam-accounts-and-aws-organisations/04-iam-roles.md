# IAM roles

* IAM users are generally designed for situations where a single principal uses that IAM user
* An IAM role is best suited to be used by an unknown number or multiple principals
* Can be used by multiple users inside an AWS account or it could be humans, applications or services inside/outside of an AWS account
* Roles are also generally used on a temporary basis. Something becomes that role for a short period of time and then stops
* A role is something that represents a level of access inside an AWS account. It's a thing that can be used, short term, by other identities

* IAM users can have identity `Permissions Policies` attached to them, either inline JSON or via attached managed policies
* IAM roles have two types of policies:
    * `Trust Policy`: controls which identites can assume that role. Can reference identities in the same account (other IAM users, other roles and AWS services) and in other AWS accounts. Can even allow anomymous usage of that role and other types of identities
    * `Permissions Policy`
