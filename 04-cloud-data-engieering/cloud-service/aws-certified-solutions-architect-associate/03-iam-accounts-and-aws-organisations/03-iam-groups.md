# IAM groups

* Are containers for IAM users and exists to make users organization easier
* Groups are not a true identity, 
    * They can't be referenced as a principal in a resource policy
    * No one can be logged into a group and they don't have credentials
* They can have policies attached to them
* There isn't a built-in all-users group inside IAM
* No nesting
* There's a limit of 300 groups per account, but this limit can be increased with a support ticket
