# AWS accounts - The basics

* An AWS account is a container for identities (users) and resources
* When creating an AWS account an account name, and unique email address and a credit card (can be used across multiple aws accounts) is provided
* Each account has its own Account Root User which has full control over all of its AWS account and any resources creted within it and can't be restricted
* Additional identities can be created inside the AWS account which can be restricted and granted FULL or LIMITED permissions via IAM (Identity and Access Management)
* AWS accounts can contain the impact of admin errors, or exploits by bad actors. Using separate accounts for separate things (DEV, TEST, PROC) or teams or products or clients is a good practice
* External identities can be granted access to the AWS account
