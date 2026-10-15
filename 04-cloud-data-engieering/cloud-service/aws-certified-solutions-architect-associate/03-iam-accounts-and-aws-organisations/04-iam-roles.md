# IAM roles

* An IAM role is best suited to be used by an unknown number or multiple principals
* Can be used by multiple users inside an AWS account or it could be humans, applications or services inside/outside of an AWS account
* Roles are also generally used on a temporary basis. Something becomes that role for a short period of time and then stops
* A role is something that represents a level of access inside an AWS account. It's a thing that can be used, short term, by other identities

* IAM roles have two types of policies:
    * `Trust Policy`: controls which identities can assume that role. Can reference identities in the same account (other IAM users, other roles and AWS services) and in other AWS accounts.
    * `Permissions Policy`
