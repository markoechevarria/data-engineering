# AWS Control Tower

* Its job is to allow Quick and Easy setup of multi-account environment
* It orchestrates AWS Organizations, AWS IAM Identity Center (AWS SSO), AWS Cloudformation, AWS Config and more to provide its functionality
* Parts
    * Landing Zone: 
        * It's a feature designed to allow anyone to implement a well-architected, multi-account environment
        * The account used to configure AWS control tower is the management account at the Landing Zone
        * Home Region is refered to the region where the product was deployed into
        * Used IAM Identity Center to provide SSO access across multiple AWS accounts within the Landing Zone
        * Handle SSO/ID Federation, Centralised Loggind and Auditing
        * When Control Tower is first set up, it creates two organizational units:
        * Users can provision new AWS accounts using Service Catalog
            * A foundational OU called Security
                * Audit Account: for uses which need access to the audit information made available by Control Tower (SNS and Cloudwatch can be configured here)
                * Log Archive Account: for users that need access to all logging information (AWS Config and AWS CloudTrail are stored within this account)
            * A custom OU called Sandbox
                * Used for testing and less rigid security situations
    * Guard Rails: 
        * Detect/mandate rules/standards across all accounts
        * There are three types: Mandatory, Strongly Recommended, Elective
        * Preventive: stop the user doing things within the accounts, are implemented using Service Control Policies
            * Are Enforced or Not enabled 
        * Detective: compliance checks, uses AWS Config rules and allows the user to check that the configuration of a given thing matches what's defined as best practice
            * Are clear, in violation or not enabled
    * Account Factory
        * Automates and Standardises account provisioning inside the custom OU
        * AWS CloudFormation is used to manage the creation of the accounts
        * AWS Config and Service Control Policies are used to implement account guardrail automatically
        * Accounts can be closed or repurposed
        * Can be fully integrated with a businessed SDLC (Software Development Life Cycle)
    * Dashboard
        * Single page oversight of the entire environment
