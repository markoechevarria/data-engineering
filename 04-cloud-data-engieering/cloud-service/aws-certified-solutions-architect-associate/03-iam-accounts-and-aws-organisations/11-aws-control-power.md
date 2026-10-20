# AWS Control Tower

* Its jobs is to allow Quick and Easy setup of multi-account environment
* Orchestrates other AWS services to provide this functionality
* It uses Organizations, IAM Identity Center, Cloudformation, Config and more
* Parts
    * Landing Zone: 
        * The multi-account environment, what most people will be interacting with
        * Handle SSO/ID Federation, Centralised Loggind and Auditing
    * Guard Rails: 
        * Detect/mandate rules/standards across all accounts
    * Account Factory
        * Automates and Standardises new account creation
    * Dashboard
        * Single page oversight of the entire environment

* The account used to configure AWS control tower is the management account at the Landing Zone
