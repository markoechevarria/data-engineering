# S3 Security (Resource Policies & ACLs)

* S3 is private by default, the only identity allowed to access S3 is the account root user

## S3 bucket policy 

* A resource policy
* ALLOW/DENY access on the same or different accounts
* ALLOW/DENY access to anonymous principals 
* Their document policies have the field "Principal" which refers to the principal who will be affected
* Bucket policy document can apply to certain Ips based on conditions, there are many conditions that can be used in Resource policies

## Access Control Lists (ACLs)

* Are a legacy way to apply security to objects or buckets
* Are a sub-resource of the object it refers
* Are inflexible and only allow very simple permissions

## Block Public Access settings

* Settings applied to all buckets with public access enabled
* They affect to all anonymous principals who tried to access the bucket 
* They are applied no matter what the resource policy says
    1. Block all public access
    2. Block public access to buckets and objects granted through new access control lists (ACLs)
    3. Block any public access granted by ACLs
