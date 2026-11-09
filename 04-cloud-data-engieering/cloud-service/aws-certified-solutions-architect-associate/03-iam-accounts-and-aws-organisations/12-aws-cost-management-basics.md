# AWS Cost Management Basics

## Cost Explorer

* Filter and group costs based on service, tag, region, cost categories, and more
* Supports granularity of monthly, daily, and hourly (costs money, requires setup)
* Includes forecasting using historical data (Enhanced Forecasts available)
* Requires preferences enabled for resource-level and multi-year data

## Cost Allocations Tags

* Helps to understand and allocate costs by team, department, product, etc
* Tags resources in AWS, then activate tags in the Billing console separately
* Activation takes up to 24 hours - and data is only collected after activation
* Two types: AWS-generated (aws:createdBy) and user-defined (user:tagname)

## Data Exports / CUR (Cost and Usage Reports)

* Most granular AWs billing data (every resource, usage type, tag and price)
* Delivered up to once a day to S3 as CSV (GZIP) or Parquet (columnar storage)
* CUR 2.0 (via Data Exports) replaces legacy CUR with a fixed, queryable schema
* Typically queried using Athena or visualised in QuickSight
