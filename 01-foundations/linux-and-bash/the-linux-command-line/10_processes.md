# 10. Processes

## How a process work

* When a system starts up, the kernel initiates a few of its own activities as processes and launches a program called init.init
* Child process: A program can launch other programs
* `ps`: used to view processes
    * `ps x`: all processes regardless of what terminal they are controlled by. It display the STAT field
        * `R`: running
        * `S`: Sleeping. It is waiting for an event
        * `D`: Uninterruptible sleep. Waiting for I/O such a disk drive
        * `T`: Stopped, the process has been instructed to stop
        * `Z`: A 'zombie' process. this child process has terminated but has not been cleanded up by its parent
        * `<`: A high-priority process.
        * `N`: A low-priority process
    * `ps aux`: Display the processes belonging to every use
        * `USER`: User Id. The ownerr of the process
        * `%CPU`: CPU usage in percent
        * `%MEM`: Memory usage in percent
        * `VSZ`: Virtual memory size
        * `RSS`: Resident set size. Amount of physical memory that process is using in kilobytes
        * `START`: Time when the process started
* `top`: displays a continuously updating display of the sytem process listed in order of process activity

* In a terminal, pressing `Ctrl-C` interrupts a program
* Adding `&` put the process in the background and return the PID
* `jobs`: list the jobs that have been launched from our terminal
* `fg %1`: return a process to the foreground
* `Ctrl-Z`: stop a process without terminating it
* `bg %1`: resume the program's execution in the background
* `kill`: used to "kill" processes

* To shut down the system: reboot, shutdown, poweroff





