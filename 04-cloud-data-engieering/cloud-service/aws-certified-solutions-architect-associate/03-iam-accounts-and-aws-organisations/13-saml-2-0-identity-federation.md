# SAML2.0 Identity Federation

* SAML 2.0 (Security Assertion Markup Language)
* Open Standard used by many Identity Providers
* Indirectly use on-premises IDs to access AWS
* SAML, an identity Federation, is the process of exchanging or swapping external identities for valid AWS credentials
* Is the process of using an identity from another identity provider outside of AWS, but still so you can access AWS resources
* When to use
    * When an enterprise-based identity provider compatible with SEML2 is being used
    * When there is an existing identity management team
* Allows a single source of identity truth in the business
* Uses IAM roles and temporary credentials with max 12-hour validity
* There needs to be bidirectional trust created betwen IAM and the on-prem IP

## How works for API access

* An application communicate with the IP to request access
* The IP access the identity store and authenticate that request, and identifies which 'roles' the identity has access to
* Inside the IP is mapped identities onto one or more roles, one identity might be able to use multiple different roles
* The application gets back an SAML assertion, a kind of token which proves the identity has been authenticated
* The application is going to communicate with AWS, specifically with the security token service, STS, using the STS assume role with SAML operation, and it passes in the SAML assertion that has been created
* The SAML assertion is exchanged for valid Temporary AWS Credentials
* The IAM Roles Assumed and Temporary Security Credentials returned to the application

## How works for Console Access

* The user authenticate against the on-premises identity store using their corporate credentials
* the IdP evaluates the user's group membership and maps them to the appropiate AWS IAM role(s) they are permitted to use
* The IdP generate a signed SAML assertion ( an document containing the user's identity and authorized role ARN) and sends back to the user's browser
* The browser posts the SAML assertion to the AWS sign-in endpoint for SAML
* AWS validates the SAML assertion, checks the established trust relationship between the IdP and the IAM SAML provider, and calls the AssumeRoleWithSAMLP API behind the scenes to generate temporary AWS security credentials
* AWS creates a sign-in token and issues a redirect URL to the browser, establishing an authenticated session for the AWS Management Console
* The user is securely logged into the AWS Management Console with permissions restricted to the assigned IAM role, valid for up to 12 hours
