# AWS Organizations

* Is a product which allows large businesses to manage multiple AWS accounts in a cost-effective way
* The structure within AWS Organizations is hierarchical, it is an inverted tree
* AWS organizations feature a service called Service Control Policies (SCPs), which lets restrict what AWS account within the organization can do
* In AWS organizations IAM roles can be used to allow IAM users to access other AWS accounts, it's a good practice to have all identities inside only one separate AWS account dedicated to handle logins
* Management Account (Master Account, Payer Account)
    * Is the standard account used to create the organization
    * Can invite other existing standard AWS account into the organization
    * Consolidate and manage the charges and billing of the Member Accounts
    * Benefits and discounts are pooled, and the organization can benefit as a whole
    * It can create new AWS accounts directly within the organization
* Member Accounts
    * Individual AWS accounts that belongs to an organization
* Organizational Root
    * Container for AWS accounts which exists at the top of the organizational structure
    * Can contain Member Accounts and Organizational Units
* Organizational Units
    * Container which can contain Member Accounts and others Organizational Units
