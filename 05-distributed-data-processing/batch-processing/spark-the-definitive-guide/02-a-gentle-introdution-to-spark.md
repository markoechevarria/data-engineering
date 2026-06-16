# Chapter 2. A Gentle introduction to Spark

## Sparks's basic Architecture
* Single machines do not have enough power and resources to perform computation on huge amounts of information.
* A cluster, or group of computers, pools the resources of many machines together, giving us the abilitity to use all the cumulative resources as if they were in a single computer.

### Spark applications
* Spark application consist of a driver processor and a set of executor processes. 
* Driver processor: 
	* Runs the main() function.
	* Maintain information about the spark application
	* Respond to a user's program or input
	* Analize, distribute and schedule work accross the executors. 
* Executors:
	* Responsibles for actually carrying out the work that the driver assigns them.
	* Each executor is responsible for executing code assigned to it by the driver, and reporting the state of the computation on that executor to the driver node.

-- Spark in adition to its cluster mode has a local mode. In local mode, the driver and executors run ( as threads ) on a individual computer insted of a cluster.

### Sparks languages apis

* Spark is primarily written in Scala, but also support Java, Python, SQL, and R

## The SparkSession

* The SparkSesion instance is the way Spark executes user-defined manipulations across the cluster
* There is one-to-one correspondence between a SparkSession and a Spark Application

## Dataframes

* The most common Structured API and simply represents a table of data with rows and columns
* The list that defines the columns and the types within those columns is called the schema
* A Spark DataFrame can span thousands of computers

### Partitions

* To allow every executor to perform work in parallel, Spark breaks up the data into chunks called partitions
* A partition is a collection of rows that sit on one physical machine in a cluster
* A DataFrame's partitions represent how data is physically distributed across the cluster of machines during execution

## Transformations

* In Spark, the core data structures are inmutable, they cannot be changed after they're created
* To "change" a DataFrame, you need to instruct Spark how you would like to modify it to do what you want
* Narrow Transformations are those for which each input partition will contribute to only one output partition, only one partition contributes to at most one output partition. With this transformations Spark automatically perform an operation called pipelining
* Wide Transformations will have input partitions contributing to many output partitions, often this is referred as shuffle whereby Spark will exchange partitions across the cluster. When a shuffle perform, Spark writes the resul to disk

### Lazy Evaluation

* Spark will wait until the very last moment to execute the graph of computation instructions
* In Spark, instead of modifying the data inmediately when you express some operation, you build up a plan of transformations that you would like to apply to your source data
* Spark compiles this plan from the raw DataFrame transformations to a streamlined physical plan that will run as efficiently as possible across the cluster

## Actions

* An action instructs Spark to compute a result from a series of transformations
* There are three types of actions
	* Actions to view data in the console
	* Actions to collect data to native objects in the respective language
	* Actions to write to output data sources

## Spark UI

* The progrss of a Job can be monitored through the Spark Web UI
* The Sparks UI displays information on the state of the Spark jobs, its environments, and cluster state

## An End-to-End example

* Spark includes the abilit to read and write from a large number of data sources
* The schema inference option means that we want Spark to take a best guess at what the schema of our DataFrame should be. Spark peeked at only a couple of rows of data to try to guess what types each column should be
* We can call `explain` on any DataFrame object to see the DataFrame's lineage (how Spark will execute this query)
* The logical plan of transformations that we build up defines a lineage for the DataFrame so that at any given point in time, Sparks knows how to recompute any partition by performing all of the operations it had before on the same input data.

### DataFrames and SQL

* Spark can run the same transformations, regardless of the language, in the exact same way
* Spark SQL can register any DataFrame as a table or view and query it using pure SQL
* To query data in SQL we should use the spark.sql function
* Comparison Spark SQL and PySpark

```
maxSql = spark.sql("""
	SELECT DEST_COUNTRY_NAME, sum(count) as destination_total
	FROM flight_data_2015
	GROUP BY DEST_COUNTRY_NAME
	ORDER BY sum(count) DESC
	LIMIT 5
""")

maxSql = flight_data_2015.\
	groupBy("DEST_COUNTRY_NAME").\
	sum("count").\
	withColumnRenamed("sum(count)", "destination_total").\
	sort(desc("destination_total")).\
	limit(5).\
	show()
```

* The execution plan is a directed acyclic graph (DAG) of transformations, each resulting in a new inmutable DataFrame
