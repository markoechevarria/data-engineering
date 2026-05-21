# Database Administration

## Configuration Files

* postgresql.conf: Controls general settings, such as memory allocation, default storage location for new databases, the IP address that PostgreSQL listens on, locations of logs, and plenty more
* pg_hba.conf: Controls acces to the server, dictatinc which users can log in to which databases, which IP addresses can conncect, and which authentitacion scheme to accept
* pg_ident.conf: maps and authenticated OS login to a a PostgreSQL user.

- Reloading: `pg_ctl reload -D data_directory`
- Reloading PostgreSQL installed as a service: `service postgresql reload`

- Restarting: `pg_ctl restart -D data_directory`
- Restarting PostgreSQL installed as a service: `service postgresql restart`

## The postgresql.conf file

* How to finetune the postgresql server wiki.postgresql.org/wiki/Tuning_Your_PostgreSQL_Server
* It is recommended edit the postgresq.auto.conf and avoid editing postgresql.conf

### Network settings in postgresql.conf
* listen_addresses: Informs PostgreSQL which IP addresses to listen on.
* port: Default to 5432
* max_connections: the maximum number of concurrent connections allowed
* log_destination: specifies the format of the logfiles
### Performance settings in postgresql.conf
* shared_buffers: allocated amount of memory shared among all connections to store recently accessed pages. Affects the speed of the queries, optimal set as much as 25% of the RAM (and less than 8GB)
* effective_cache_size: an estimate of how much memory PostgreSQL expect the operating system to devote to it, With much lower than available RAM, the planner may forgo using indexes. Optimal setting to half of the RAM ( with a dedicated server )
* work_men: maximum amount of memory allocated for each operation such as sorting, hash join, and table scans. With many users this setting should be low.
* maintenance_work_men: total memory allocated for housekeeping activities such as vacuuming ( pruning records marked for deletion). This shouldn't be higher than 1 GB
* max_parallel_workers_per_garther: determine the maximum parallel worker threads that can be spawned for each gather operation. Deault setting is 0 ( parallelism turned off ), should be least than max_worker_processes.

### Changing the postgresql.conf settings

Edit postgres.conf: `ALTER SYSTEM SET workd_mem = '500MB';`
Reload the server: `SELECT pg_reload_conf();`

## The pg_hba.conf file

Controls which IP addresses and users can connect to the database. dictated the authentication protocol the client must follow

### Authentication methods

* trust: no password is needed
* md5: requires an md5-encrypted password to connect
* password: uses clear-text password authentication
* ident: uses pg_ident.conf to check whether the OS account of the user trying to connect has a mapping to a PostgreSQL account
* peer: uses the OS name of the user from the kernel
* cert: stipulates that connections use SSL

## Managing connections

To cancel running queries and terminate connection:

1. Retrive a list of recent connections and process `SELECT * FROM pg_stat_activity;`
2. Cancel active queries on a conection with PID `SELECT pg_cancel_backend( PID );`
3. Terminate the connection: `SELECT pg_terminate_backend( PID );`

### Operational parameters 

* deadlock_timeout: amount of time a deadlocked query should wait before giving up
* statement_timeout: amount of time a query can run before it is forced to cancel
* lock_timeout: amount of time a query should wait for a lock before giving up
* idle_in_transaction_session_timeout: amount of time a transactioncan stay in an idle state before it is terminated

## Roles

### Creating Login Roles

* During the setup PostgreSQL creates a single login rol with the name postgres
* Creating login roles: `CREATE ROLE marko LOGIN PASSWORD 'marko' CREATEDB;`, CREATEDB grants database creation privilege to the new role
* Create a user with superuser privileges: `CREATE ROLE marko LOGIN PASSWORD 'marko' SUPERUSER`
* To create roles that cannot log in omit the `LOGIN PASSWORD` clause

### Creating Group Roles

* Group roles generally cannot log in, generally they server as containers for other roles
* Create a group role `CREATE ROLE marko_group INHRIT`
* Add members to a group role `GRANT marko_group TO marko`
* Give superuser rights to a group: `ALTER ROLE marko_group SUPERUSER`
* Give superuser rights to a user: `SET ROLE marko_group`
* SET ROLE change the current_user while SET SESSION AUTHORIZATION also changes the session_user

## Database Creation

* Minimum SQL command to create a database
* Basic syntax to create a database modeled after a specific template
* Make a database a template

```
CREATE DATABASE template_table ( field_1 INT, field_2 INT );
ALTER DATABASE template_table WITH IS_TEMPLATE TRUE;

CREATE DATABASE real_table TEMPLATE template_table;
```
## Using Schemas

* Schemas orgnize a database into logical groups.
* Objects must have unique names within a schema but need not be unique across the database

```
CREATE SCHEMA test_schema;
CREATE TABLE test_schema.test_table;
```

## Privileges

* PostgreSQL has a few dozens of privileges 
* Most privileges must have a context

```
CREATE ROLE test_role LOGIN PASSWORD 'test_role_password';
CREATE DATABASE test_role_database WITH owner = test_role;
```

* GRANT: primary means to assign privileges ` GRANT some_privilege TO some_role;`
* Grant privileges on all objects of a specific type `GRANT SELECT, REFRENCES, TRIGGER ON ALL TABLES IN SCHEMA schema_name TO PUBLIC;`
* Revoke privileges `REVOKE EXECUTION ON ALL FUNCTIONS IN SCHEMA schema_name FROM PUBLIC;`


