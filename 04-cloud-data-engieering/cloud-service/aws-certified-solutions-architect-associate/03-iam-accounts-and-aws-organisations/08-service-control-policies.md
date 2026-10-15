# Service Control Policies (SCP)

* SCPs are a feature of AWS organizations, can be used to restrict AWS accounts
* It's a policy document (a JSON document) that can be attached to a organization as a whole
* Can be attached to the root container, to one or more organizational units, or to individual AWS accounts
* SCP inherit down the organization tree
* The management account is never affected by SCPs

* SCPs are account permissions boundaries, they limit what the account (including account root user) can do
* SCPs don't greate any permissions 

* SCPs allows
    * Deny list (default): Allow by default and block certain services
    * Allow list: Block by default and allow certain services

* When SCPs are enabled on an organization, AWS apply a default policy called 'full AWS access' that is which is applied to the organization and all OUs
