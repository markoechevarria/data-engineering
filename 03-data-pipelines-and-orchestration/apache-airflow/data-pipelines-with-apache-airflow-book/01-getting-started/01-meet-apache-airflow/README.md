## Data pipelines

Tasks or actions that need to be executed to achieve a desired result

Data pipelines can be represented as DAGs, which clearly define tasks and their dependencies. These graphs can be executed efficiently, taking advantage of any parallelism inherent in the dependency structure.

Although many workflow managers have been developed over the years for executing graphs of tasks, Airflow has several key features that makes it uniquely suited for implementing efficient, batch-oriented data pipelines.

Airflow consists of three core components: the webserver, the schedule and the worke processes, which work together to schedule tasks from your data pipeline and help you monitor their results
