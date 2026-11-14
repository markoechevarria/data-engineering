# Databricks Architecture Overview

## Control Plane

* Handles all the backend services required for the Databricks Platform
1. Databricks User Interface: Where users interact with Databricks through a browser-based interface
2. Cluster manager: Is responsible for managing and provisioning compute resources when users create clusters or interact with existing clusters to scale them up and down
3. Unity Catalog: Provides data governance and helps manage access and permissions for the data
4. Queries and code: Storage for queries and workspace data. This storage is mainly used for storing various workspace-related metadata like notebooks and job run details

## Compute Plane

* Where the data processing takes place
* Databricks supports two types of compute
    1. Classic Compute: Databricks provisions clusters directly within the customer's cloud subscription. The computer resources such as virtual machines are deployed and managed within the cloud account
    2. Serverless Compute: Runs on the Databricks subscription with Databricks allocating resources from its pool of virtual machines already made available. This significally recudes cluster startup time compared to classic compute

## Workspace Cloud Storage

* Set up in the cloud subscription when a Databricks workspace is created
    * In Azure, it's the Azure Data Lake Storage Gen 2
    * In AWS, it's the S3 Bucket
    * In GCP it is Google Cloud Storage
* Is used to store system data such as notebook revisions, job run details, spark logs, and much more
* Can be used to store temporary data
* Is deleted when the workspace is deleted

## Architecture by location

* Control plane and Serverless compute both exist in the Databricks Subscription
* Classic compute plane and the workspace cloud storage are located in the cloud subscription
* Through either of compute types, we can access and process data stored in the cloud or on-premises applications
