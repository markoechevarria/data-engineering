# Cloudformation

* A tool which lets create, update and delete infraestructure in AWS

## CloudFormation templates

* A Cloudformation template is a text file that acts as a blueprint for building and managing AWS infraestructure
* Its written either in yaml or json
* Cloudformation main parts:

    1. Resources: All templates have a list of resources, at least one. It tells CloudFormation what to do

    2. Description: Let the author of the template add a description. Used to give some details of what the template does

    3. AWSTemplateFormatVersion: The way AWS allows for exteding the standards over time. If it's provided, them the Description field should be after it

    4. Metadata: Can control how the different things in the CloudFormation template are pressented through the console UI and do other advanced things

    5. Parameters: is where fields which prompt the user for more information can be declared
        * Size of the instances to create
        * The name of something
        * The number of availability zones to use

    6. Mappings: Allows to create lookup tables

    7. Conditions: Allow decision making in the template

    8. Outputs: Once the template is finished, it can present output based on what's being created

* Resources inside a template are called logical resources
    * A logical resource has a type
    * Logical resouces have properties

* CloudFormation use the template to cretes a stack (which contains all logical resources)
* When a Cloudformation use a template to crete a stack
    * Cloudformation scans the template
    * Cloudformation creates a stack with logical resources inside
    * Cloudformation creates physical resources which match
