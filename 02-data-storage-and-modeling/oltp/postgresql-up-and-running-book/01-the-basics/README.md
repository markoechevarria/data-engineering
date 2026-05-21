# PostgreSQL Basics

* PostgreSQL is an enterprise-class relational database management system
* PostgreSQL allows you to write stored procedures and functions in numerous programming languages
* Not only does PostgreSQL come with a large built-in set data types, but you can define additional data types to suit your needs.
* PostgreSQL automatically creates types from any tables you define.

## PostgreSQL Database Objects

* Databases: Each PostgreSQL service houses many individual databases
* Schemas: Inmediate next level of organization within each database. Most databases objects first belong to a schema, which belongs to a database
* Tables: Workhourses of any database. Tables are first citizens of their respectives schemas. PostgreSQL tables are inheritable and, whenever you create a table, PostgreSQL automatically creates an accompanying custom data type
* Views: Views are a level of abstraction from tables, generally readonly.
* Extensions: Allow developers to package functions, data types, casts, custom index types, tables, attribute variables, etc
* Functions: Custom functions to handle data manipulation, perform complex calculations, or wrap similar functionality
* Languages: Create functions using a PL ( SQL, PS/pgSQL and C).
* Operators: Symbolically named aliases for functions.
* Foreign tables and foreign data wrappers: 
    * Foreign tables: virtual tables linked to data outside a PostgreSQL database like CSV files, a table on another Postgresql server, a table on a different product, a NoSQL database.
    * Foreign data wrappers: Facilitate the magic handshake between PostgreSQL and external data sources
* Triggers and trigger functions: 
    * Triggers: detect data-change events
    * Trigger functions: respond to triggers 
* Catalogs: system of schemas that store PostgreSQL built-in functions and metada. Every database contains two catalogs: pg_catalog ( holds all functions, tables, system views, casts, and types packages ) and information_schema ( offers views exposing metadata in a format dictated by the ANSI SQL standard )
* Type: data types such as integers, characters, arrys, blobs, etc
* Full text search: natural language-based search
* Casts: prescribe how to convert from one data type to another
* Sequences: Controls the autoincrementation of a serial data type
* Rules: Instructions to rewrite an SQL prior to execution




