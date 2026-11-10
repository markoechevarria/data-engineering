# Cloudformation

* AWS's infrastructure as Code (IaC) service, which let's create update and delete infraestructure

## CloudFormation templates

* A Cloudformation template is a text file that acts as a blueprint for building and managing AWS infraestructure
* Its written either in yaml or json
* Cloudformation main template sections:
    1. AWSTemplateFormatVersion: The version of the template format (helps AWS extend standards over time). If it's provided, then the Description field should be after it
    2. Description: Let the author of the template add a description. Used to give some details of what the template does
    3. Parameters: Fields that prompt the user for more information at deployment time
        * Size of the instances to create
        * The name of something
        * The number of availability zones to use
    4. Mappings: Allows to create conditional lookup tables
    5. Conditions: Controls whether certain resources are created based on specific rules
    6. Transform: Used for macros or serverless applications (AWS SAM).
    7. Resources:  All templates have a list of resources, at least one. It tells CloudFormation what to do
    8. Metadata: Can control how the different things in the CloudFormation template are pressented through the console UI and do other advanced things
    9. Outputs: Returns data (like URLs, IP addresses, or IDs) after the stack is successfully created

## Logical vs. Physical Resources:

- Logical Resources: The names and definitions declared inside the template code.
- Physical Resources: The actual AWS resources created in your account when the stack runs (tied to the logical resources).

## How Stacks work

* CloudFormation uses a template to create a Stack (a collection of AWS resources managed as a single unit)
* Process:
    1. Cloudformation scans and validate the template
    2. Cloudformation creates the stack and evaluates the logical resources
    3. Cloudformation calls underlying AWS APIs to create the matching physical resources.
