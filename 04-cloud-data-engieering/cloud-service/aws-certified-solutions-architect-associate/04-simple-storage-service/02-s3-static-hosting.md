# S3 Static Hosting

* This feature allows access via HTTP
* Index and Error documents are set
* When this feature is enabled, a Website Endpoint is created
* The name is created influenced by the bucket name and the region the bucket is in
* An custom domain can be used only if the name of the bucket matches the domain

## Common Examples

* Offloading: take the heavy, static parts of a website away from the primary web application servers and let S3 serve them instead
* Out-of-band page: a website hosted entirely separate from the primary network infraestructure, designed to staly online if the main application suffers an outage or undergoes scheduled maintenance

## S3 pricing

* Storing: is expressed as a per gygabite month fee
* Transfer: is expressed as a per gygabite of data transfered in and out. Transfer data into s3 is free
* Request data: different operations (PUT, GET, LIST, etc) have different costs per 1000 operations
