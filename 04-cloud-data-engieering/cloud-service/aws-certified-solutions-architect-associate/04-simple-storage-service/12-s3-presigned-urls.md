# S3 Presigned URLs

* A way to give another person or application access to an object inside an S3 bucket using someone else's credentials

## Workflow 

* An authenticated user with permissions over a bucket make a request to S3 to generate a pre-signed URL
* The user needs to provide their credentials, the bucket name, an object key, and a expiry date and time, and the HTTP method that will be used (GET or PUT)
* S3 creates a presigned URL and return it. The URL have encoded within it the dtails that the user provided
* The URL is passed to the unauthenticated users to let them access the s3 bucket
* The holder of the URL is interacting with S3 as the user who generated it

## Considerations

* An user can create a URL for an object they have no access to
* When using the URL, the permissions match the identity which generated it
* Access denied could them the generating identity never had access
* When using IAM roles, the URL will stop working when temporary credentials expire
