# Delta Lakehouse overview

* New, open data management architecture that combines the flexibility, cost-efficiency and scale of Data Lakes with the data management and ACID transactions of Data Warehouses, enabling business intelligence (BI) and machine learning (ML) on all data

## Data Warehouse

* A centralized place to store all organizational data
* Analysts and business managers could then access the data through BI reports
* Allows to make decisions based on the full set of information available in the company
    * Operational data from within the organization
    * Some large DWs also gathered external data
* Data received in a data warehouse was usually structured (couldn't process unstructured data such as images and videos), such as SQL tables or semi-structured (JSON or XML files)
* Data received goes through a process called ETL (Extract-Transform-Load) to be loaded into the DW
* Complex DWs also had data marts which:
    * Focused on specific subject areas or regions of the business
    * Contained cleaned, validated, and enhanced data, often aggregated to provide key insight like key performance indicators or KPIs


* In the early 2000s, data volumes increased dramatically and new type of unstructured data like videos, images and text files became important for decision making
* Data was only loaded after its quality was checked and transformed, which leds to longer development times to add new data into the data warehouse
* DW were built on traditional relational databases or massive parallel processing engines or MPP engines, which used propietary file formats and could create vendor lock in
* Traditional on premises DWs were hard to scale, sometimes requiring large migrations projects to increase capacity
* Storage was expensive with this traditional solutions, it was impossible to expand storage independently of computing resources
* Traditional DWs didn't provide enough support for data science, machine learning, and AI workloads

## Data Lake 

* Were introduced around the year 2011 to address some of the DWs challenges
