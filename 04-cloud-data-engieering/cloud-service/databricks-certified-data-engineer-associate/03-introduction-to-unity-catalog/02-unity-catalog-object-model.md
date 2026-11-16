# Unity Catalog Object Model

1. Metastore

* Top level container for all metadata in the Unity Catalog
* Lives with the Databricks account level, and only one Metastore can be created per cloud region
* One or more Databricks workspaces can be attached to the Metastore
* Can be paired with a container in ADLs Gen2 for Default storage at the time of creation

2. Catalog

* Newly added to Unity Catalog, Hive Metastore didn't have the concept of catalogs
* Logical container within Metastore to organize datasets
* Each catalog may contain one or more schemas or databases

3. Schemas

* Next level container within Catalogs
* Schemas and Databases are the same. Schema is used
* Each schema may contain one or more volumes, tables, view and functions 

* Volumes: logical volumes which are high level abstraction to the containers
    * External: Unity Catalog-governed storage volume registered against an existing directory in the cloud object storage
    * Managed: Unity Catalog-governed storage volume where Databricks automatically determines and manages the underlying cloud storage location
* Tables: collections of data organized by rows and columns
    * External: Only metadata are managed by Databricks. The underlying data is managed by the cloud provider. Data can have any format
    * Managed: Unity Catalog manages both the metadata and the data for the table. All are in delta table format

4. Storage, credential and external location allow to access a cloud storage or data lake other than the default storage attached to the metastore

5. Service credentials are used to hold the credentials of external cloud services altogether

6. Connections represent credentials that give read only access to an external database

7. Share, Recipient and Provider are used to handle Delta sharing

8. Catalog (hive_metastore)

* A pseudo catalog created by Databricks in every Databricks workspace
* Schemas, Tables, Views and functions can be created
