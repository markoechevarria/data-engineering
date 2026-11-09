# S3 Client vs Server-Side Encryption (SSE)

* Encryption In-Transit: Protects the data while it traveles over the network, can use HTTP and HTTPS with TLS
* Client-Side Encryption
    * The objects being uploaded are encrypted by the client before they ever leave, so the the data being uploaded is in ciphertext
* Server-Side Encryption
    * The objects aren't initially encrypted.
    * Once the data actually hits S3, then it is going to be encrypted by the S3 serverso
* Server-side encryption is mandatory by AWS, every object in S3 is encrypted at rest (SSE-S3 by default, but you can choose the type)
