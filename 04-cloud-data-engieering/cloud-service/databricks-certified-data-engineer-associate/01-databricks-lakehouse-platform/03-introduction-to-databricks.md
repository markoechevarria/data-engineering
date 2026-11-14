# Introduction to Databricks

* At the core is the open source distributed compute engine Apache Spark
* Databricks was founded by the creators of Apache Spark to make working with Spark easier by providing the essential management layers
* It's available on all major cloud platforms including Microsoft Azure, AWS and Google Cloud

## Apache Spark

* Is a lightning-fast unified analytics engineer for big data processing and machine learning
* Developed at UP Berkeley in 2009 and open sourced in 2010, under Apache License since 2013
* Was designed to address the limitations of Hadoop, which was slow and infefficient for interactive and iterative computing tasks; in contrast Spark provides simpler and faster APIs that are easier to work with
* It can be up to 100 times faster than Hadoop, by utilizing in-memory computing and varios optimizations
* Runs on a distributed computing platform
* Has a unified engine that supports both batch and streaming workloads
* Includes built-in libraries for SQL queries, machine learning, and graph processing

## Databricks features

* Clusters: Databricks allows to spin up clusters with just a few clicks. Different runtime options can be choosed, whether it is for general purpose use, memory optimized processing, or GPU support for machine learning tasks
* Workspace/Notebook: Databricks provides an integrated Jupyter style notebook IDE that allows to create and run applications, collaborate with colleagues, and connect with version control tools such as git
* Administration controls: To help manage user access to workspaces and clusters ensuring secure usage
* Optimized Spark Engine: Databricks provides the spark runtime, which is highly optimized for Databricks platform and known to be up to five times faster than vanilla Apache Spark
* Photon: Databricks comes with a vectorized query engine called photon, which provides extremely fast query performance, up to eight times improvement on the standard Databricks runtime
* Unity Catalog: Databrikcs enables users to create and manage databases and tables using hive, Metastore, or Unity Catalog. Unity Catalog also supports data lineage and provides improved governance
* Delta Lake: Offers robut support for asset transactions, which ensures data reliability and integrity
* Delta Live Tables: A declarative ETL framework that helps create reliable data pipelines with ease
* Workflows: buil-in feature that helps schedule and orchestrate tasks and pipelines as required
* SQL Warehouse: Databricks SQL provides a SQL based analytical environment to explore data, create dashboards, schedule a regular refresh of the dashboard, etc
* MLFlow: Helps manage the machine learning lifecycle, including experimentation, deployment model, registry, etc
* DatabricksIQ: AI assistant to help develop and debug code, add commands, and create dashborards

## Databricks and Cloud Platforms

* Databricks is available on all three major cloud platforms (Azure, AWS, GCP). The integration between the cloud platforms and Databricks is quite similar, except the Azure hosts Databricks as a first party service. Using Azure with Databricks, provideds a unified billing and direct support from Microsoft for all services, including Azure services and Databricks
* Databrikcs leverages on the security and the governance services from the cloud providers such as Azure Active Directory, AWS IAM
* Databricks integrates with storage services such as Azure Data Lake Storage Gen2, AWS S3, etc
* The underlying virtual machines for the Databrikcs clusters are provided by the cloud providers
* Monitoring Solutions services provided by the cloud providers can be used to help track and analize the Databricks workloads
* Databricks integrates with DevOps services offered by the cloud providers such as Azure DevOps to help enable continuous integration and continuous deployment, or CI/CD

## Databricks User Interface Overview

* Workspace: Act as a container for folders, notebooks, libraries, and files for the project. Each user has their own workspace folder. There is also a shared workspace that can be used for collaboration
* Recents: Shows the assets recently accesed
* Catalog: Allows to view and interact with the tables, views, volumes, files, etc
* Jobs and Pipelines: let's create data ingestion and ETL pipelines, as well as Lakeflow jobs. Lakeflow jobs allows to schedule notebooks and pipelines to run automatically
* Compute: where can be created and managed various compute types, such as all purpose compute, jobs compute, SQl warehouses, etc. Cluster pools can be created to reduce compute startup time and compute policies that lets administer control of how the clusters are created by restricting things like cluster size, instant types, auto termination, etc
* Jobs Runs: takes to the same page as the Jobs and Pipelines
* Data Ingestion: Allows create tables from local files, upload data into Databricks, and integrate with third party ingestion tools
