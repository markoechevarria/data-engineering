# Service-linked roles

* Is an IAM role linked to a specific AWS service
* They provides a set of permissions that a service needs to interact with other AWS services on behalf of the owner
* Service might create/delete the role or allow the owner to during the setup or within IAM
* Service-linked roles can't be deleted until it is no longer required

* Role separation is where one might give one group of people the ability to create roles and another group the ability to use them
