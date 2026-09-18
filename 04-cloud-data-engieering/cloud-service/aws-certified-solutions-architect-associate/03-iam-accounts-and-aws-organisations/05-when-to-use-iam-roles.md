# When to use IAM roles

* For AWS services themselves:
    * AWS services use Service Roles or Service-Linked Roles to interact with other AWS resources securely on your behalf

* For emergency or out of the usual situations
    * IAM roles are commonly used to establish temporary, highly privileged "break-glass" access for emergency incident response, avoiding the security risks of permanent administrator credentials

* Adding AWS into an existing corporate environment
    * IAM roles enable Cross-Account Access (allowing external AWS accounts to securely interact with the resources) and Identity Federation without sharing long-term credentials

* When there are more thatn 5000 users
    * While identity federation is critical for managing large organizations without creating individual IAM users, there is no specific user count threshold (such as 5,000) required to use it
