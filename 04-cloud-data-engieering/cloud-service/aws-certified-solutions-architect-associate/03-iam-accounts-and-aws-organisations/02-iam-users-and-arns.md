# IAM users

* IAM Users are an identity used for anything requiring long-term AWS access e.g. Humans, Applications or Service account

1. IAM starts with a principal, which represents an entity trying to access an AWS account. A principal is a physical person, application, service or process
2. The principal makes requests to IAM to interact with resources. It needs to authenticate against an identity within IAM
3. The principal is now known as an authenticated identity
4. Once the principal becomes an authenticated identity then AWS knows which policies apply to the identity

* Authentication is how a principal can prove to IAM that it is the identity that it claims to be
* Authorization is IAM checking the statements that apply to that identity and either allowing or denying that access
* IAM users are limited to 5000 per account
* An IAM User can be a member of at most 10 groups
* When limits are reached, IAM roles or Identity federation can be used, it means using own existing identities rather than using IAM users

# Amazon Resource Names (ARNs) 

* Uniquely identify resources within any AWS accounts
* ARNs allows refers to a single resource or in some cases, a group of resources using wild cards
* ARNs can always identify single resources, whether they're individual resources in the same account or in different accounts

```
arn:partition:service:region:account-id:resource-id
arn:partition:service:region:account-id:resource-type/resource-id
arn:partition:service:region:account-id:resource-type:resource-id
arn:aws:s3:::bucket-name        # this refers to the bucket
arn:aws:s3:::bucket-name/*      # this refers to the objects in the bucket
```
