# S3 Server Side Encryption

* Buckets aren't encrypted, objects are
* Each object can be encrypted with different encryption types
* A Type of Encryption can be configured at the bucket level. This is going the determine the type of encyrptiong what will be used by objects inside the bucket

## Types of S3 SSE

* Server-Side Encryption with Customer-Provided Keys (SSE-C)
    * The customer is responsible for the keys that will be using for encryption and decryption
    * The algorithmic process is done by AWS
* Server-side Encryption with Amazon S3-Managed Keys (SSE-S3)
    * This is the default
    * AWS handle both the encryption process as well as the key generation and management
    * When an object is uploaded to S3, it is going to be encrypted by a key which is unique for every single object
    * S3 has a S3 Key which use to encrypt the Object key of all objects
* Server-side Encryption with KMS Keys Stored in AWS Key Management Service (SSE-KMS)
    * First it's needed to create a KMS key, or the aws/s3 (AWs automatically creates it)
    * S3 request from KMS a key generated using the KMS key configured
    * S3 uses the plaintext key to encrypt the data and store the cyphertext version of that key
* Dual-Layer Server-Side encryption with AWS KMS keys (DSSE-KMS)
    * Used in very specific situations
    * Before the data is actually written to disk, an extra layer of encryption occurs
    * S3 is going to use itw own encryption key to encrypt the already encrypted data 
