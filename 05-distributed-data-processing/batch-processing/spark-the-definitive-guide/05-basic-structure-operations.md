# Chapter 5

* A DataFrame consists of a series of records (like rows in a table), that are of type Row, and a number of columns (like columns in a spredsheet) that represent a computation expression that can be performed on each individual record in the Dataset.

## Schemas

* A schema defines the column names and types of a DataFrame
* We can either let a data source define the schema ( schema-on-read ) or we can define it explicitly ourselves.
* A schema is a StructType made up of a number of fields, StructFields, that have a name, type, a Boolean flag which specifies whehter that colum can contain missing or null values, and users users can optionally specify associated metadata with that column

```
from pyspark.sql.types import StructField, StructType, StringType, LongType

myManualSchema = StructType([
	StructField("DEST_COUNTRY_NAME", StringType(), True),
	StructField("ORIGIN_COUNTRY_NAME", StringType(), True),
	StructField("count", LongType(), False, metadata={"hello":"world"})
])

df = spark.read.format("json").schema(myManualSchema).load("/data/flight-data/json/2015-summary.json")
```

## Columns and Expressions

* Columns can be selected, manipulated and removed from DataFrames, and these operations are represented as expressions

### Columns

* They can be constructed by using the col or column functions

```
from pyspark.sql.funtions import col, column
col("someColumnName")
column("someColumnName")
```

* To refere to a specific DataFrame's column use `df.col("count")`

### Expressions

* An expression is a set of transformations on one or more values in a record in a DataFrame
* The simplest expression case is a DataFrame column reference `expr("someCol")`

#### Columns and Expressions

* If you use col() and want to perform transformations on that column, you must perform those on that column reference.
* The expr function can actually parse transformations and columns references from a string and can be subsequently be passed into further transformations
* expr("someCol - 5") == col("someCol") - 5 == expr("someCol") - 5

```
from pyspark.sql.functions import expr

expr(" ( ( (someCol + 5) * 200 ) - 6 ) < otherCol")
```

#### Accessing a DataFrame's columns

* If you want to programatically access columns, use the property columns

```
spark.read.format("json").load("/data/flight-data/json/2015-summary.json").columns
```

## Records and Rows

* Each Row in a DataFrame is a single record
* Spark represent each row as an object of type Row
'df.first()'

### Creating Rows

* Row can be created manually instantiating a Row object with the values that belong in each column

```
from pyspark.sql import Row
myRow = Row("Hello", None, 1, False)
```

## DataFrame transformations

* In DataFrames:
	* We can add rows or columns
	* We can remove rows or columns
	* We can transform a row into a column (or vice versa)
	* We can change the order of rows based on the values in columns

### Creating DataFrames