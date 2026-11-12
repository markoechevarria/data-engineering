# Resource Access Manager (RAM)

* Resources of each account in an Organization are isolated
* Duplicate copies across an organization mean extra costs, admnistration and many more issues
* Create one, share it and the owner keeps control
* Allows to share resources with other accounts, avoiding duplication
* Ram allows create a `resource share` which is resource + principal + permissions
* Not everything is shareable through RAM
* Share with account, Org/OU, IAM role/user
* Allows AWS managed permissiones and customer managed permissions
* When a resource shared is created, it will send that share as an invite to the principle defined. But if AWS organizations are used, then from the management account of that organization it's needed to accesss RAM and switch on the AWS organization share setting, that will mean that principles within the organization get access automatically

## Considerations

* RAM vs StackSets -> share vs copy
* Regional service, a resource share is created in a specific region, and that is where it will be accepted
* RAM is free, there's no charge for creating shares or sharing resources
* When a resource is shared with an organization, membership is dynamic, if an account joins an organization or is moved onto an organizational unit, then the member will gain access automatically, the flip side is also true
* An account can't re-share what's shared with it
