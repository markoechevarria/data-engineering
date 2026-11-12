# IAM Identity Center

* Manage SSO Access - AWS Accounts (requires Org instance) and external Applications
* SSO (Single Sign-On) allow users to have just one username and password
* Identity Center replaces many of the use cases for manual SAML2-based Federation

* Flexible Identity Store: where the identities are stored, all identity-related data, username, passwords, first names, departments and things like that
    * Identity Center (default): build-in Identity Store. Used to manage access to all AWS account without any identity System
    * AWS Managed Microsoft AD: vida the directory service product
    * On-premises Microsoft AD (Two way trust or AD Connector)
    * External Identity Provider - SAML2.0
* AWS accounts need to be in an AWS organization
* IAM identity center inside the AWS organization is used to provide a single identity access to multiple accounts
* The identity center is configured with something called an Organization Instance which is always deployed on the Management Account
* Delegated Administration means that a different AWS accountthat the administrators can go through to manage Identity Center
* Account Instance: deploy Identity Center to a single account when there's no AWS organization, cannot manage access to AWS organization, instead it only allow access to Applications
* Identity Center integrates with a range of workplace `Identity Sources` ranging from built-in Identity Center identities through to self-managed on-premises Active Directory
* Identity Center is the AWS preferred workplace identity solution - it handles SSO & permissions for AWS accounts and exernal applications
