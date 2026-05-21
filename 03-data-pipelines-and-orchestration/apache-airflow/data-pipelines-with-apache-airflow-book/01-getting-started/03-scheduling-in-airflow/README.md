## Scheduling in Airflow

Cron syntax

* * * * *
minute ( 0 - 59 )
hour ( 0 - 23 )
day of the month ( 1 - 31 )
month ( 1 - 12 )
day of the week ( 0 - 6 )

0 0 * * MON, WED, FRI
0 0 * * MON-FRI
0 0,12 * * *

@once -> once and only once
@hourly -> once an hour at the beginning of the hour
@daily -> once a day at midnight
@weekly -> once a week at midnight on sunday morning
@monthly -> once a month at midnight on the first day of the month
@yearly -> once a year at midnight on januray 1

DAGs can run at regular intervals by setting the schedule interval
The work for an interval is started at the end of the interval
The schedule interval can be configured with cron and timedelta expressions
Data can be processed incrementally by dinamically setting variables with templating
The executiion date referes to the start datetime of the interval, not to the actual time of execution 
A DAG can be run back in time with backfilling
Idempotency ensures tasks can be rerun while producing the sme output results
