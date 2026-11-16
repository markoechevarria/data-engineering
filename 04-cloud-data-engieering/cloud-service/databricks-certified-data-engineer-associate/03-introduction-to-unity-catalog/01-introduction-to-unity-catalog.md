# Introduction to Unity Catalog

## Data Access Patterns - Legacy Solutions

* Databricks File System (DBFS)
    * Distributed file system fully integrated with Databricks, useful for accessing file containing unstructured data
    * Provided an abstraction layer over the cloud storage, allowing access data using Unix-like file paths
    * Can be access using dbutils file system utility a from a Databricks Cluster of a job

* Hive Metastore
    * Used for accessing structured or semi structured data
    * Tables can be created over the data stored
    * Hive Metastore registers the tables in the Metastore and stores additional information about the data files such as columns, data types, partitions, etc, which enables to query the data through SQL queries
    * Allows create views to contain summaries of filtered data and also functions to abstract the tranformation logic
    * Enables to restrict or grant access to the Metastore objects to the user based on their roles
    * Lack fine granted access control (row and column level access), audit logging, lineage support for multi-cloud environments, etc

## Unity Catalog

* Metastore Unity Catalog allows to create tables, functions and views on structured data
* Volume: An abstraction layer on top of the files in the cloud storage, it's the recommended approach for reading and writing files in Lakehouse, especially files containing unstructured data
* Unified solution for accessing files as well as table objects
* Offers data lineage, data security, data governance, etrc
