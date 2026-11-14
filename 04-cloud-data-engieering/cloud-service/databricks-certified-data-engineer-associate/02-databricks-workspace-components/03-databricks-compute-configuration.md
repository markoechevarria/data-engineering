# Databricks Compute Configuration

1. Simple/Multi node

* Multi-node clusters 
    * Include one driver node and one or more worker nodes
    * When a Spark job run on a multi-node cluster, the driver distributes the tasks to the worker nodes, allowing for parallel execution
    * Provides horizontal scalability based on the workload demands
    * Ideal for larger workloads
* Single Node clusters
    * Contain only a driver node with no worker nodes
    * The same node acts as both the drive and the worker
    * It cannot be horizontally scaled, making it unsuitable for large ETL workloads
    * Are designed for lightweight machine learning and data analysis tasks that don't require distributed computing
    * Are also incompatible with process isoltaion and they're not intended for shared usage among multiple users or workloads

2. Access Mode

* A security feature that allows who can use the compute and what data they can access
* There are two types of access modes available
    1. Dedicated or Single User Access Mode
        * Allows only a single user to access the cluster
        * It supports all four languages: Python, SQL, Scala and R
    2. Standard or Shared Acess Model
        * Enables sharing the cluster among multiple users while providing process isolation
        * Each process operates in its own environment, preventing one process from accessing another process's data or credentials
        * Is available only on premium workspaces
        * It supports Python, Scala and SQL

3. Databricks Runtime

* The set of core libraries that run on Databricks clusters
* Two types of runtimes
    1. Databricks Runtime
        * Includes an optimized version of Apache Spark with various supporting libraries
    2. Databricks Runtime ML
        * Includes popular machine learning libraries such as PyTorh, Keras, Tensorflow, and XGBoost
* Both allows to enable or disable Photon, which is a vectorized query engine which accelerated Apache Spark workloads

4. Auto termination

* Useful feature to prevent unnecesary cost on ideal clusters
* It automatically terminates a cluster if it remains unused for a specified period of time. The default is set to 120 minutes
* Users can specify a value between 10 and 43200 mins (30 days) as the duration

5. Auto Scaling

* When creating a multi-node cluster we can specify the minimum and the maximum number of worker nodes
* This feature automatically adjusts the number of nodes based on the workloads, optimizing cluster utilization
* Useful when workloads are unpredictable or fluctuate during the process
* To save costs, we can opt for Spark Instances for worker nodes
* Driver nodes are always on-demand nodes
* When Spark instances become unavailable, Databricks will attempt to acquire replacements or switch to on-demand instances as a fallback

6. Cluster VM Type/Size

* Azure offers a range of VM types which Databricks groups into:
    1. Memory optimized: are suitable for memory-intensive workloads, like ML workloads that cache large datasets
    2. Compute optimized: are ideal for structured streaming applications where peak time procesing rates are very critical as well for distributed analytic and data science workloads
    3. Storage optimized: are recommended for use cases requiring high disk throughput and I-O
    4. General Purpose: are suitable for enterprise-grade applications and analytics with in-memory caching
    5. GPU accelerated» are designed for DL models that are both data and compute intensive

7. Cluster policy

* Help prevents missconfigurations by allowing administrators to set restrictions and assign them to users or groups
