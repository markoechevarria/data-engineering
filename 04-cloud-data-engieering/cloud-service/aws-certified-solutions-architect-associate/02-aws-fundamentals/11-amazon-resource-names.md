# Amazon Resource Name (ARN)

* Allows to uniquely identitfy resources within any AWS account
* ARNs allows refers to a single resource or in some cases, a group of resources using wild cards
* ARNs can always identify single resources, whether they're individual resources in the same account or in different accounts

```
arn:partition:service:region:account-id:resource-id
arn:partition:service:region:account-id:resource-type/resource-id
arn:partition:service:region:account-id:resource-type:resource-id
arn:aws:s3:::bucket-name        # this refers to the bucket
arn:aws:s3:::bucket-name/*      # this refers to the objects in the bucket
```
