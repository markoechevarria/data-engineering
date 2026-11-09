# Service-linked roles

* Is an IAM role linked to a specific AWS service
* They provides a set of permissions that a service needs to interact with other AWS services on behalf of the owner
* They are perdefined and created automatically by the AWS Service or then can be created by the user during the setup or within IAM
* They are managed by AWS and cannot be edited
* Service-linked roles can't be deleted until it is no longer required
* Role separation is where one might give one group of people the ability to create roles and another group the ability to use them

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "arn:aws:iam::*:role/aws-service-role/SERVICE-NAME.amazonaws.com/SERVICE-LINKED-ROLE-NAME-PREFIX*",
            "Condition": {"StringLike": { "iam:AWSServiceName": "SERVICE-NAME.amazonaws.com"}}
        },
        {
            "Effect": "Allow",
            "Action": [

            ],
            "Resource": "arn:aws:iam::*:role/aws-service-role/SERVICE-NAME.amazonaws.com/SERVICE-LINKED-ROLE-NAME-PREFIX*"
        }
    ]
}
```
