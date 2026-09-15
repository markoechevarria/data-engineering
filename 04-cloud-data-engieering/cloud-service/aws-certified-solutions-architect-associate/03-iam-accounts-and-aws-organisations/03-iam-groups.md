# IAM groups

* Iam groups, are containers for IAM users
* They exists to make users organization easier
* No one can be logged into group, and IAM groups doesn't have credentials
* Groups can have policies attached to them (inline and managed policies)
* There isn't a built-in all-users group inside IAM
* No nesting
* There's a limit of 300 groups per account, but these can be increased with a support ticket

* Groups are not a true identity, they can't be referenced as a principal in a policy
* A resource policy cannot grant access to an IAM group
