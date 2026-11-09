# AWS Lambda

* Function-as-a-Service (FaaS) - short running and focussed
* Lambda Function: a piece of code Lambda runs
* Functions use a runtime
* Functions are loaded and run in an execution environment
* The environment has a direct memory (indirect CPU) allocation
* Billed for the duration that a function runs and per request
* A key part of Serverless architectures

## Architecture

* Lambda Function is a deployment package which Lambda executeso* Types of deployment packages:
    * Zip archive: supports 50MB zipped and 250mb unzipped
    * Container image: give up to 10GB
* Every time Lambda runs, a new execution execution environment is created
* Memory can be defined from 128mb to 10240mb. But vCPU can't be controlled directly
* 512MB storage available as `/tmp` up to 10240MB
* Function timeout of 900s (15min)
* Security for Lambda function is controlled by using execution roles, and these are just IAM roles which are assumed by the Lambda function

## Use Cases

* Serverless Applications (S3, API, Gateway, Lambda)
* File Processing (S3, S3 Events, Lambda)
* Databrase Triggers (DynamoDB, Streams, Lambda)
* Serverless CRON (EventBridge + Lambda)
* Realtime Stream Data Processing (Kinesis + Lambda)

## Networking

* Default Networking
    * Run inside a secure VPC owned and managed entirely by AWS
    * Outbund internet Access: The function can freely call any public internet endpoint, API, or public AWS service (like Amazon S3 or DynamoDB)
    * Private resources: It cannot connect to resources residing inside the private, isolated virtual networs without routing traffic through public endpoints
* VPC-attached networking
    * AWS lambda creates a Hyperplane ENI (Elastic Network Interface) inside the designated subnets. The function still runs in the Lambda service VPC, but all its network egress is tunneled directly into the VPC using AWS Hyperplane technology
    * Outbound internet access: Once attached to a VPC, the functions loses default public internet access
    * To restore internet access, we must route the function's traffic through a Private Subnet mapped to a NAT Gateway. Placing a Lambda function directly in a public subnet with an internet Gateway will not give it internet access, because Lambda does not assign public IP addresses to its execution environments
    * To access other AWS services privately, VPC Endponts (AWS PrivateLink) can be used to securely connect the function to services like Secret Manager of SQS without passing trafic over the public internet

## Security

* An `Execution role` needs to be provided for an environment to access any AWS product or services. It's a role assumed by Lambda which should have a trust policyt which trusts Lambda
* Lambda resource policy controls WHAT services and accounts can INVOKE lambda functions

## Logging

* Lambda uses CloudWatch, CloudWatch Logs & X-Ray
* Any logging information generated from Lambda executions goes into CloudWatch Logs. CloudWatch Log requires permissions via Execution Role
* Metrics such as invocations success/failure, retries, latency are stored in CloudWatch
* Lambda can be integrated with X-Ray for distributed tracing

## Invocation

* Synchronous invocationo
    * Commnad Lince or API or by triggering the functions own function URL
    * Directing invoking a Lambda function
    * The lambda function will be provided with some data and it executes that data
    * The CLI or API is waiting for the response, it needs to wait until the Lambda function completes its execution
    * When the Lambda function finishes, it returns the data as well as whether itis a success or a failure
    * Also happens if Lambda is used indirectly via the API gateway which is the use case for many serverless architecture
    * Errors or Retries have to be handled within the client
* Asynchronous invocation
    * Used typically when AWS services themselves invoke Lambda functions
    * Invocator isn't waiting for any kind of response. The event is generated and S3 stops tracking
    * If the Lambda function errors, Lambda will retry between 0 and 2 times (configurable). Lambda handles the retry logic
    * The lambda function needs to be idempotent reprocessing a result should have the same end state
    * Lambda functionc can be configured to send any events which it can't process after those automatic tries to a dead letter queue or DLQ for short which can be used for diagnostic processing
    * Lambda can create destinations, so events processed by Lambda functions can be delievered to another destination such as SQS, SNS, S3 (only failure), another Lambda function or EventBridge
* Event Source mappings
    * Typically used on streams or queues which don't support event generation to invoke Lambda (Kinesis, DynamoDB streams, SQS, etc)
    * Is responsible for polling queues or streams looking for new data and getting back source batches. This batches are broken up as required all based on a batch size and then they are sent to a Lambda function as event batches. By default, event batches are processed OK or FAIL as a batch
    * The source service isn't delivering an event, instead is the event source maping component is reading from that source and so the event source mapping does need and uses permissions from the Lambda execution role to access that source service, so even if a Lambda function receives an event batch

## Versioning

* It's possible to have specific versions of Lambda functions
* A version is the code + the configuration of the lambda function, so the resources, any environment variables and other configuration information
* It's inmutable - code and most configuration never change once published and has its own ARN
* `$LATEST` is the unpublished, mutable working version
* Aliases (DEV, STAGE, PROD) point at a version - can be changed

## Startup Time

* Execution context: a small container which has allocated the resources that runs the Lambda code
* Cold Start: is a full creation and configuration including function code download
* Warm Start: if the same Lambda function is invoker again without too much of a gap, then it is possible that Lambda will use the same execution environment
* Provisioed concurrency can be used. AWS sill create and keep X contests warm and ready to use
* `/temp` can be used to pre-download things within the execution environment
* Anything declared outside of the Lambda Function handler will be avaiable for any another invocations of that Lambda Function
