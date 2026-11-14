# Delta Lakehouse overview

* New, open data management architecture that combines the flexibility, cost-efficiency and scale of Data Lakes with the data management and ACID transactions of Data Warehouses, enabling business intelligence (BI) and machine learning (ML) on all data

## Data Warehouse

* A centralized place to store all organizational data
* Allows to make decisions based on the full set of information available in the company
    * Operational data from within the organization
    * Some large DWs also gathered external data
* Data received in a data warehouse was usually structured (couldn't process unstructured data such as images and videos), such as SQL tables or semi-structured (JSON or XML files)
* Data received goes through a process called ETL (Extract-Transform-Load) to be loaded into the DW
* Complex DWs also had data marts which:
    * Focused on specific subject areas or regions of the business
    * Contained cleaned, validated, and enhanced data, often aggregated to provide key insight like key performance indicators or KPIs
* Analysts and business managers could then access the data through BI reports
* Limitations
    * Increased Data Volume & Variety: data volumes increased dramatically and new type of unstructured data like videos, images and text files became important for decision making
    * Longer time to Ingest new data: data was only loaded after its quality was checked and transformed, which leds to longer development times to add new data into the DW
    * Propietary Data Formats/Vendor Lock In: DWs were built on traditional relational databases or massive parallel processing (MPP) engines, which used propietary file formats
    * Scalability Issues: Traditional on premises DWs were hard to scale, sometimes requiring large migrations projects to increase capacity
    * High Storage Costs: Storage was expensive with this traditional solutions, it was impossible to expand storage independently of computing resources
    * Limited Support for Advanced Analytics: Traditional DWs didn't provide enough support for data science, machine learning, and AI workloads

## Data Lake 

* Were introduced around the year 2011 to address some of the DWs challenges
* Designed to handle structured, semi-structured and unstructured data (roughly 90% of the data available today in a DL house arquitecture)
* Raw data is ingested directly into the DL without any intial cleansing or transformation (faster ingestion times)
* Were built on cheap storage solutions like HDFS and cloud object stores such as Amazon S3 and Azure Data Lake Storage Gen2, which kept the costs low
* They also utilized open source file formats like parquet, ORC and Avro
* Supported data sciences and machine learnin workloads by providing access to both raw and transformed data
* Companies often copied a subset of the data from the DL to a DW because DLs were too slow for interactive BI reports and lacked proper data governance, this leds to a complex architecture with too many moving parts
* Limitations
    * No support for ACID transactions: No support for Atomicity, Consistency, Isolation and Durability, essential for reliable data management
    * Partial Data Loads: Fail jobs could leave behind partially loaded files requiring additional cleanup processes during reruns
    * Inconsistency Reads: Leading to the possibility of users accesing partially written data, which compromised reliability
    * Complicated Data Corrections: no direct support for updates to correct or update data. Developers had to partition the files and rewrite entire partitions, which was both time consuming as well as error prone
    * No Rollback Capability: No way to roll back changes, which mades it difficult to recover from failures
    * GDPR challenges: Since the DLs didn't support deletions well, entire files sometimes had to be rewritten to remove an individual's data
    * No data versioning: DL lacked version control, which made it harder to track changes, perform rollbacks, or ensure data governance
    * Poor BI performance and Support: DLs struggled to provide fast, interactive query performance and lacked adequate support for basic needs such as security and governance
    * Complex to set-up: Setting up and managing data lakes was complex and requiredd significant expertise in a DL
    * Streaming and batch data needed to be processed separately, leading to complex lamda architectures

## Data Lakehouse

* Combines the best features of both data warehouses and data lakes
* Designed to support BI and data science, machine learning and AI workloads
* Similar to DLs, both operational and external data can be ingested into a DLH
* A DLH is issentially a DL with built-in acid transactions, controls and data governance capabilities. DLs achieve this using the file format Delta Lake and a data governance solution called Unity Catalog, with ACID support offered by the Delta Lake file format, we can seamlessl combine streaming and batch workloads, eliminating the need for complex Lambda architectures
* Advantages:
    * Handles All types of data
    * Run on cost effective cloud object storage, such as Amazon S3 or Azure Data Lake Storage Gen2
    * Uses Open file formats
    * Support for All workloads
    * Allow direct integration with BI tools
    * Provide ACID support, data versioning, and history, thus preventing the creation of unreliable data
    * Offer better performance compared to traditional DLs
    * Simple architecture by removing the need for lambda arquitecture and reducing the reliance on separate DWs
