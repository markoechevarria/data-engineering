# 11. The environment

* The shell maintains a body of information during our shell session called the environment
* `printenv`: to see what is stored in the environment
* `printenv USER`: list the value of a specific variable
* `set`: display both the shell and environment variables, as well as defined shell functions
* `echo $HOME`: to view the contents of a variable
* `alias` displays the aliases

* When the log on the system, the bash program starts and reads a series of configuration scripts called *startup files*. which define the default environment shared by all users

* To add directories to the PATH or define additional environment variables, place those changes in .bash_profile
