# 3. Exploring the system

* Commands are often followed by one or more options that modify their behavior. They usually have the structure `command -options arguments`

* `ls -a`: list all 
* `ls -A`: list all except the `.` and `..` 
* `ls -l`: display results in long format 
    * -rw-r--r-- : access right to the file
    * 1: file's number of hard links
    * root: the username of the file's owner
    * root: the name of the group that owns the file
    * 32059: size of the file in bytes
    * 2017-04-03 11:05 : date and time of the file's last modification
    * 00-cd-over.odf : name of the file

* `file filename`: print a brief description of the file's contents
* `less filename`: to view text files

## Directories found on Linux Systems

* `/`: the root directory
* `/bin`: contains binaries that must be present for the sytem to boot and run
* `/boot`: contains the linux kernel, initial RAM disk image and the boot loader
* `/dev`: contains device nodes
* `/etc`: contains all the system-wide configuration files, also contains a collection of shell scripts that start each of the sytem services at boot time
* `/home`: in normal configurations, each user is given a directory here
* `/lib`: shared library files used by the core system programs
* `/media`: on modern linux systems contain the mount points for removable media 
* `/mnt`: in older directory contains mount points for removable devices
* `/opt`: used to install "optional" software
* `/root`: the home directory for the root account
* `/tmp`: is intended for the storage of temporary
* `/usr`: contains all the programs and support files used by regular users 
* `/var`: is where data that is likely to change is stored
