# PassRole Security Model

* The `iam:PassRole` security model in AWS controls whether an identity (such as a user or another role) has permission to hand an IAM role over to an AWS service (such as Amazon EC2, AWS Lambda, or Amazon ECS) so the service can assume it.

## Authorization Requirements

* Identity-Based Policy (User/Principal): The principal (user or role) initiating the action must have explicit iam:PassRole permission in their policy to pass the specific target role.
* Service Trust Policy (Role): The IAM role being passed must have a trust relationship (AssumeRole policy) that explicitly allows the target AWS service (e.g., ://amazonaws.com or ://amazonaws.com) to assume it.
* Service Action Permission (User/Principal): The principal must have permission to perform the resource creation or modification action itself (e.g., ec2:RunInstances, lambda:CreateFunction, or cloudformation:CreateStack).
