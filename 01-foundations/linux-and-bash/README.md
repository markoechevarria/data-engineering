# Linux and bash

Content about command line, shell scripting and Linux essential commands

* ## [The linux Command Line book](the-linux-command-line/)

    * Learning the Shell: How to navigate the filesystem, create and delete files/directories, manage file permissions, and customize your command-line environment.
    * Common Tasks & Utilities: Searching for files, managing packages, connecting to storage, networking, and processing text with tools like grep and tar.
    * The Power of the Command Line: How to combine small, single-purpose tools using "pipes" and redirection to build complex, powerful workflows.
    * Shell Scripting: A beginner-friendly programming tutorial teaching you how to write full shell scripts to automate repetitive system tasks.

* ## [Projects](projects/)

    #### 1. Filesystem & Navigation Challenges:  Build a Fake Data Lake

    ```
    data-lake/
    ├── raw/
    │   ├── sales/
    │   ├── users/
    │   └── logs/
    ├── staging/
    ├── processed/
    ├── archive/
    └── scripts/
    ```

    * Use mkdir -p
    * Create 100 fake CSV files with loops
    * Name files dynamically with dates
    * Move files older than 30 days to archive
    * Compress archived files with tar + gzip

    #### 2. Log Processing: Analyze Web Server Logs

    Download a sample Apache or Nginx log.

    Then answer:

    * Top 10 IP addresses
    * Most common HTTP status codes
    * Count requests per hour
    * Find all 500 errors
    * Extract only POST requests
    * Find suspicious IPs making >100 requests


    #### 3. CSV Data Engineering Tasks: Build a Mini ETL in Bash

    * Create CSVs: id,name,country,salary
    * Remove malformed rows
    * Filter salaries > 5000
    * Convert country names to uppercase
    * Join two CSVs
    * Generate summary stats
    * Save outputs to processed/

    #### 4. Process Management Scenarios: Simulate a Broken Server

    ```
    while true; do
    echo "running"
    done
    ```

    * Run it in background.
    * Find PID
    * Kill gracefully
    * Kill forcefully
    * Monitor CPU usage
    * Redirect logs
    * Run detached with nohup
    * Schedule cleanup with cron

    #### 5. Permissions & Multi-User Practice: Simulate a Team Environment

    * Create users: alice, bob, etl_service
    * Create shared group
    * Restrict access to raw data
    * Allow read-only access
    * Create executable scripts only admins can modify

    #### 6. Shell Scripting Project (Very Important): Automated Data Ingestion Script

    * Watches an incoming/ folder
    * Validates CSV format
    * Moves bad files to rejected/
    * Compresses valid files
    * Creates logs
    * Generates ingestion reports
    * Sends terminal alerts

    #### 7. SSH & Remote Operations: Use a VM or another machine.

    * SSH into remote server
    * Transfer files with scp
    * Sync directories with rsync
    * Run remote commands
    * Configure SSH keys
    * Disable password login (optional)

    #### 8. Monitoring & Disk Management: Investigate a “Full Disk”

    * Create large fake files: `fallocate -l 2G bigfile.bin`
    * Find largest directories
    * Find large files
    * Check inode usage
    * Compress logs
    * Clean temp files

    #### 9. Build a Full Fake Data Pipeline: You receive raw CSV files every day.

    Build a bash-based pipeline that:

    * Receives files
    * Validates schema
    * Cleans data
    * Archives originals
    * Produces transformed outputs
    * Logs every step
    * Handles failures
    * Schedules execution with cron

    Directory structure:

    ```
    pipeline/
    ├── incoming/
    ├── processed/
    ├── rejected/
    ├── archive/
    ├── logs/
    └── scripts/
    ```

    #### 10. “Production Incident” Exercises

    Scenario A — Log Explosion

    A log file grows to 40GB.

    * identify cause
    * truncate safely
    * rotate logs
    * compress old logs