# 9. Permissions

* `id`: Display user identity
* `chmod`: Change a file’s mode
* `umask`: Set the default file permissions
* `su`: Run a shell as another user
* `sudo`: Execute a command as another user
* `chown`: Change a file’s owner
* `chgrp`: Change a file’s group ownership
* `passwd`: Change a user’s password

## Owners, group members, and everybody else

* In Linux a user may own files and directories.
* Users can belong to a group consisting of one or more users who are given acces to files and directories by their owner
* An owner may also grant some set of access rights to everybody, which is referred to as the world

## Reading, Writing and executing

* The first 10 characters of the listing are the file attributes
* The first of these characters is the file type (`-`: a regular file, `d`: a directory, `l` :a simbolic link)
* The remaining nine characters of the file attributes, represent the read, write, and execute permission for thte file's owner, the file's group owner, and everybody else
    * `r`: allow a files to be opened and read, and a directory contents to be listed
    * `w`: allows a file to be written to or truncated, allows files within a directory to be created, deleted and renamed
    * `x`: allows a file to be treated as a program and executed, allow a directory to be entered

* `chmod`: change file mode
* `unmask`: set default permissions

## Changing identities

* `su [-[l]] [user]`: run a shell with substritute user and groups ids
* `sudo`: allow an ordinary user to execute commands as a different user (usuarlly the superuser)

* `chown [owner][:[group]] file`: used to change the owner and group owner of a file or directory

## Changing password

* `passwd [user]`: to change the password







