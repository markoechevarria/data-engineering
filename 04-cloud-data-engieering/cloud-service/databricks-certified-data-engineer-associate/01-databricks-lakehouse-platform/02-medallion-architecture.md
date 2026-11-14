# Medallion Architecture

* Data Architecture used in the Data Lakehouse
* It's not an architectural pattern, but rather a data design pattern
* Data fllows through layers, and quality improves as data progresses through each layer

## Layer Structure

1. Bronze
    * Typically contains raw data as received from the various data sources
    * Data undergoes minimal to no transformation at most
    * Some additional metadata, such as load, timestamp, or name of the file, may be added for tracking
    * By not transforming the data, a historical record of all the data received can be maintain, making it easy to replay the data if any pipeline issue occur later
    * Supports fast ingestion of high volume and high velocity data
2. Silver
    * Holds filtered, cleansed, and enriched data with a structure applied and schema either enforced or evolver to maintain consistency
    * Data undergoes quality checks where invalid records are removed, column values are standarized, duplicates are eliminated, and missing values are either replaced or removed
    * Any required context or descriptions are added to the data
    * Results in structured, high quality and reliable data
    * The data is suitable for DS, ML and AI workloads
3. Gold
    * Business level aggregated data
    * Data from the silver layer is further aggregated and enriched with additional context to make it ready for high level business reporting and analysis
    * Used for advanced analytics and applications where needed

## Benefits

* Improves data lineage and traceability of the data by moving the data throug the clearly defined data layers. It becomes easier to track where the data has come from and how it's transformed and used in applications
* Helps enforce data governance and compliance policies such as GDPR, CcpA, etc
* Each layer has a defined meaning and granularity of the data, which helps define compliance policies such as retention policies
* Allows for processing only new and changed data received at the DLH, which supports incremental processing
* Enhanced performance and Scalability, allows better workload management for each of the layers and create scalable solutions
* Gives better control over security, such as defining role based access control to ensure only authorized users can access secure and sensitive data
