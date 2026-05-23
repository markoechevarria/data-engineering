# Chapter 4. Structured Api Overview

* The Structured APIs are a tool for manipulating all sorts of data.

## DataFrames and Datasets

* Are distributed table-like collections with well-defined rows and columns, represent inmutable, lazily evaluated plans that specify what operations to appl to data residing at a location to generate some input

## Schemas

* Defines the column names and types of a DataFrame.
* They can be defined manually or readed from a data source

## Structured Spark Types

* Spark uses an engine called Catalyst that maintains its own type information through the planning and processing of work
* Spark will convert an expression written in an input language to Spark's internal Catalyst representation of that same type information. 

### DataFrames versus Datasets

* Withing the Structured APIs, there are the "untyped" DataFrames and the "typed" Datasets
* DataFrames have types, but Spark maintains them completely and only checks wheter those types line up to those specified in the schema at runtime.
* Datasets check whether types conform to the specification at compile time. They are only availabe to JVM based languages.

### Columns

* Represent a simple type. They can be thought of as columns in a table

### Rows

* Is a record of data.
* Each record in a DataFrame must be of type Row

### Spark types

* Spark has a large number of internal type representations

## Overview of Structured API execution

* Steps of the execution of a single structured API query from user code to executed code:
	1 Write  DataFrame/Dataset/SQL code
	2 If valid code, Spark convers this to a Logical Plan
	3 Spark transform this Logical Plan to a Physical Plan, checking for optimizations along the way
	4 Spark then executes this Physical Plan (RDD manipulation) on the cluster.
* The user code is submitted to Spark. The code passes through the CAtalyst Optimizer, which decides how the code should be executed and lays out a plan for doing so before, finally, the code is run and the result is returned to the user.

### Logical Planning

* The logical Planning only represents a set of abstract tranformations, convert the user's code into the most optimized version.

* It convert the user code into a unresolverd logical plan
* Spark uses the catalog (a repository of all table and DataFrame information), to resolve columns and tables in the analyzer
* If the analyzer can resolve it , the result is passed through the Catalyst Optimizer, a collection of rules that attempt to optimizer the logical plan by pushing down predicates or selections. This create the Optimized Logical Plan

## Physical Planning

* Specifies how the logical plan will execute on the cluster by generating different physical execution strategies and comparing them thorugh a cost model
* Physical Planning results in a serie of RDDs and transformations
* Spark is refered as a compiler, it take queries in DataFrames, Datasets, and  SQL and compiles them into RDD transformations for you

## Execution

* Upon selecting a physical plan, Spark runs all of this code over RDDs
* Spark performs further optimizations at runtime, generating native Java bytecode
* Finally the result is returned to the user