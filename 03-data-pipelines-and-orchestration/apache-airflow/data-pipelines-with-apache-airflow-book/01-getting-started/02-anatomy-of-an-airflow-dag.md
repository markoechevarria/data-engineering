# 02. Anatomy of an Airflow DAG

## Writting a Airflow DAG

* Airflow allows split a large job, which consists of one or more steps, into individual “tasks” that together form a DAG. Multiple tasks can be run in parallel, and tasks can run different technologies

Workflow in Airflow are represented in DAGs
Operators represent a single unit of work
Airflow contains an array of operators both for generic and specific types of work
The Airflow UI offers a graph view for viewing the DAG structure and tree view for viewing DAG runs over time
Failed tasks can be restarted anywhere in the DAG
