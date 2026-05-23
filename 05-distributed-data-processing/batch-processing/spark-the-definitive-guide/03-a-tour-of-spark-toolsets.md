# Chapter 3. A tour of Spark toolsets

* Spark is composed of primitives ( the lower-level APIs and the Structured APIs ) and then a series of standard libraires for additional functionality
* Spark libraries support a variety of different tasks, from grapth analysis and machine learning to streaming and integrations with a host of computing and storage systems. 

## Running Production Applications

* spark-submit is a built-in command-line tool that lets you send your application code to a cluster and launch it to execute there
* Command example: `./bin/spark-submit --master local ./examples/src/main/python/pi.py 10`

## Datasets: Type-Safe structured APIs

* DataFrames are a distributed collections of objects of type Row that can hold various types of tabular data
* The Dataset API give users the ability to assign a Java/Scala class to the records within a DataFrame and manipulate it as a collection of types objects, similar to a Java ArrayLIst or Scala Seq

## Structured Streaming

* Structured Streaming is a high-level API for stream processing, it allow take the same operations that you perform in batch mode using Spark's structured APIAs and run them in a streaming fashion
* Spark stuctured streaming example

```
streamingDataFrame = spark.readStream\
	.schema(staticSchema)\
	.option("maxFilesPerTrigger", 1)\
	.format("csv")\
	.option("header", "true")\
	.load("/data/retail-data/by-day/*.csv")

purchaseByCustomerPerHour = streamingDataFrame\
	.selectExpr(
		"CustomerId", 
		"(UnitPrice * Quantity) as total_cost", 
		"InvoiceDate")\
	.groupBy( 
		col("CustomerId"), window(col("InvoiceDate")), "1 day" 
	)\
	.sum("total_cost")

purchaseByCustomerPerHour.writeStream\
	.format("memory")\
	.queryName("customer_purchases")\
	.outputMode("complete")'
	.start()
```

## Machine Learning and Advanced Analytics

* Spark has the ability to perform large-scale machine learning with a built-in library called MLlib, which allows for preprocessing, munging, training of models, and making predictions at scale on data.


## Lower Level APIs

* Spark includes a number of lower-level primitives to allow for arbitrary Java and Python object manipulation via Resilient Distributed Datasets (RDDs)

## SparkR

* Is a tool for running R on Spark. 