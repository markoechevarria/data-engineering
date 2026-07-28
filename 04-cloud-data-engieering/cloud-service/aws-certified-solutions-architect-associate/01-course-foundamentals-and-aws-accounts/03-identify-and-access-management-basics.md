# Identify and Access Management (IAM) Basics

* The root user associated with the AWS account, and has full unrestricted access to tha account
* In most real-world situations is wanted to granted access to all people on the organization access to the AWS account, and is wanted to restrict this access based on persons, groups and applications. This is called List Privilege Access

* IAM does not have cost
* IAM is an globally resiliant service, any data is secure accross all AWS regions
* IAM let the Root user do anything on the account
* Inside IAM other identities can be created, and them can be granted some access 

## Types of Identify Objects

* User: Humans or applications that need access to the account
* Group: Collection of related users (e.g. development team, finance or HR)
* Role: Can be used by AWS services, or for granting external access to the account

## IAM policy

* Object or document which can be used to allow or denied access to AWS services when they are attached to IAM users, groups or roles

## IAM three main jobs

1. Manage Identities - An ID Provider (IDP) : lets create, modified and deleted identites such as users and roles
2. Authenticate: Prove that one is who claims to be
3. Authorize: Allow or deny access to resources
