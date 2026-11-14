# Databricks Compute

* The term compute refers to a cluster of virtual machines
* A Databricks cluster typically consists of a driver node and one or more worker nodes
* The **Driver Node** is responsible for coordinating the work, while the **worker nodes** perform the actual data processing

## Serverless compute

* Is a fully managed compute option provided by Databricks
* With serverless compute, Databricks provisions and manages the underlying infraestructure, and the compute resources run in a Databricks managed cloud environment
* Databricks maintains a pool of ready-to-use compute resources, which means serverless compute starts very quickly with minimal wait time. The environment is automatically configured with a Databricks managed runtime, and the compute scales up and down automatically based on the workload
* Serverless compute uses execution-based billing. We're only charged while the code is running
* Once the task or the query completes, Databricks automatically releases the resources back to the pool, and the billing stops
* Serverless compute is production-ready for many common workloads, such as notebooks, jobs and SQL workloads
* Benefits:
    * Faster startup times
    * Reduced operational overhead
    * Improved productivity
* Limitations
    * Less control over the low-level configurations
    * Fewer customization options available

## Classic Compute

* Is fully controlled by the customer
* User is responsible for configuring and managing the cluster. This includes choosing Databricks runtime version, selecting the virtual machine types, defining the number of worker nodes, and configuring the auto-scaling behavior
* Provides maximum flexibility and control, which is useful when workloads require specific configurations or advanced customizations
* There are two types:
    1. All Purpose cluster
        * Is created manually, either through the Databricks UI, the CLI, or the API
        * Are persistnet, and they can be terminated and restarted at any point in time
        * Are suitable for interactive and ad hoc analysis workloads
        * Can be shared among many users, they're well suited for collaborative data analysis
        * Are more expensive to run
    2. Job Cluster
        * Is created automatically when a scheduled or automated job starts running
        * Are terminated at the end of each job. They cannot be restarted, they are no longer usable once the job has completed
        * Are suitable for automated workloads, such as running an ETL pipeline or a ML workload at regular intervals
        * Are isolated and dedicated only to the job being executed
        * Are more cheaper
