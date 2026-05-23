# Chapter 1. What is Apache Spark

* Apache Spark is a unifided computing engine and a set of libraries for parallel data processing on computer clusters.
* Unified: Spark's key driving goal is to offer a unified platform for writing data big applications. It's designed to support a wide range of data analytics tools rangin from Sql queries to machine learning and streaming computation.
* Computing engine: Sparks handles loading data from storage systems and performing computation on it, not permanent storage as the end itself.
* Libraries: Spark's libraries built on its design as a unified engine to provide a unified API form common data analysis tasks. Spark includes libraries for SQL and structured data (Spark SQL), machine learning (MLlib), stream processing (Spark streaming and Structured Streaming), and grapth analytics (GraphX). 

## The big data problem

* Computers became faster every year through processor speed increases, most of applications were designed to run only on a single processor
* The one single processor improved trend stopped around 2005, due to hard limits in heat dissipation, so the hardware developers switched toward adding more parallel CPU cores all runnign at the same speed.
* Nowadays collecting data is extremely inexpensive, but processing requires large and parallel computation