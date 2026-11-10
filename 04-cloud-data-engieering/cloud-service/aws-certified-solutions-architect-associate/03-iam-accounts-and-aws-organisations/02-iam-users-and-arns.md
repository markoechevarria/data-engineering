# IAM users

* IAM Users are an identity used for anything requiring long-term AWS access
* AWS supports temporary credentials
* Service quotas apply to identity and access management resources
* Authentication is how a principal can prove to IAM that it is the identity that it claims to be
* Authorization is IAM checking the statements that apply to that identity and either allowing or denying that access
* IAM users are limited to 5000 per account
* An IAM User can be a member of at most 10 groups
* When limits are reached, IAM roles or Identity federation can be used, it means using own existing identities rather than using IAM users

## IAM users process

1. IAM starts with a principal, which represents an entity trying to access an AWS account. A principal is a physical person, application, service or process
2. The principal makes requests to IAM to interact with resources. It needs to authenticate against an identity within IAM
3. The principal is now known as an authenticated identity
4. Once the principal becomes an authenticated identity then AWS knows which policies apply to the identity
