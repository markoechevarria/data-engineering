# S3 Performance Optimization

## Multipart Upload

### Problem

* By default, when an object is uploaded to S3, it is loaded as a single blob of data in a single stream. The file becomes an object and it's uploaded using the PutObject API call and placed in the bucket
* If a stream fails, the whole upload fails, and the only recovery from it is a full restart of the entire upload
* The PUT method have limited the speed liability of the upload, because of the single stream of data
* There's a limit of 5GB of data as maximum per upload

### Advantage

* Improve the speed and reliability of uploads to S3
* Data is broken up into individual parts 
* The minimum size for using multipart upload is 100MB
* An upload can be split into a maximum of 10,000 parts
* Each individual part can range in size between 5MB and 5GB, and the last part can be smaller thatn 5MB if needed
* Each individual part is treated as its own isolated upload, each part can fail and can be restarted in isolation
* The Transfer rate of the whole upload is the sum of all the individual parts

## S3 Accelerated Transfer

### Problem

* It is possible for the data not follow a "direct" path to the bucket destination, and the data can slow down as it moves from hop to hop

### Advantage

* Transfer accelartion uses the network of AWS edge locations, which are located in lots of convenient locations globally
* This configuration needs to be enabled at the bucket-level (off by default)
* Restrictions for enable Accelarated Transfer
    * Bucket name can not contain periods 
    * Needs to be DNS compatible in its naming
* The uploading go to the closest best performing AWS edge location, and the data is transfered over the AWS global network, which tends to be a direct link
* Use the accelearte endpoint in the app/client (standard or IPv6)
