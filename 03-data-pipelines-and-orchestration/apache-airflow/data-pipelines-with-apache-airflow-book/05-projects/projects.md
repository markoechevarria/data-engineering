## Resilient API → Warehouse Pipeline

Build a fault-tolerant ingestion pipeline from a public API ( Weather API, Crypto prices, GitHub events ) into a database.
API → raw storage → transform → PostgreSQL (or BigQuery)

Airflow Concepts:
* DAG scheduling (hourly/daily)
* Task dependencies
* Retries + exponential backoff
* Task Groups
* XCom (only where appropriate)
* Connections (store API keys properly)

Requirements:
* Handle: pagination, rate limits, API failures
* Ensure idempotency (no duplicate data)
* Add data validation step
* Store raw + cleaned data separately

## Multi-DAG Data Platform (ELT style)

Build a modular data platform with multiple DAGs that interact.

Dags:

* DAG 1 — Ingestion: Pull data from API OR files (S3/local)
* DAG 2 — Transformation: Clean + normalize data -> Possibly use SQL transformations
* DAG 3 — Analytics / reporting: Aggregate metrics -> Generate reports or dashboards data

Airflow Concepts:
* Cross-DAG dependencies
* Sensors (wait for data availability)
* TaskGroups or dynamic tasks
* Variables & config-driven pipelines
* Backfills

Requirements
* Use Dockerized Airflow
* Use LocalExecutor or CeleryExecutor
* Add: SLA monitoring and failure alerts (email/Slack)
* Separate environments: dev vs prod configs

## Event-Driven + Dynamic Pipelines (Production-grade)

Simulate a modern data platform with dynamic workflows
New data arrives → pipeline adapts automatically

New files land in storage (simulate S3)
Airflow detects them
Dynamically creates tasks to process each files

Airflow Concepts:
* Dynamic DAG generation
* Event-driven scheduling (sensors or triggers)
* Task mapping (dynamic task expansion)
* Custom operators (optional but strong signal)
* DAG versioning concepts

Requirements:
* Process variable number of inputs
* Add: schema validation and failure isolation (one file fails ≠ whole DAG fails)
* Implement: logging strategy and debugging workflow



