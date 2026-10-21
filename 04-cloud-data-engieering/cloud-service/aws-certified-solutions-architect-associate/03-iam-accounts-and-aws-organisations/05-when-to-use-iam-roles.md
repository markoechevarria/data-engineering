# When to use IAM roles

* **For AWS services themselves**: AWS services use Service Roles or Service-Linked Roles to interact with other AWS resources securely on your behalf

* **For emergency or out of the usual situations**: IAM roles are commonly used to establish temporary, highly privileged "break-glass" access for emergency incident response

* **Adding AWS into an existing corporate environment**: IAM roles enable Cross-Account Access (allowing external AWS accounts to securely interact with the resources) and Identity Federation without sharing long-term credentials
