# AWS Organizations

* Is a product which allows larger businesses to manage multiple AWS accounts in a cost-effective way
* Without AWS organizations many large business faced a situtation where they need to manage many AWS accounts

* An standard account is used to create an organization within AWS
* The standard account becomes the Management Account (formerly Master Account) for the organization
* The Management account can invite other exist standard AWS accounts into the organization, so they become Member Accounts of that organization

* The structure within AWS Organizations is hierarchical, it is an inverted tree
* At the top is the Organization Root, which is a container for AWS accounts which exists at the top of the organizational structure
* Organization Root can contain other containers known as organizational units or OUs and this OU can contain AWS accounts or Member Accounts or the Management Account or they can contain other organizational units

* The Member Accounts passed their billing through to the Management Account of the organization
* Consolidation of reservations and volume discounts 
* AWS organizations feature a service called Service Control Policies (SCPs), which lets restrict what AWS account within the organization can do

* New AWS accounts can be created within an AWS Organization
* In AWS organizations IAM roles can be used to allow IAM users to access other AWS accounts, it's a good practice to have all identities inside only one AWS account
