# 4. Manipulating files and directories

* wildcards allows select filenames based on patterns of characters
    * \* : matches any characters
    * \? : matches any single character
    * \[characters\] : matches any character that is a member of the set characters
    * \[\!characters\] : matches any character that is not a member of the set characters
    * \[\[\:class\:\]\] : matches any character that is a member of the specified class

* `mkdir`: used to create directories
* `cp`: copies files or directories
    * \-a flag: copy with all of their attributes
    * \-i flag: before overwriting prompt the user for confirmation
    * \-r flag: recursiverly copy directories and their contents
    * \-u flag: only copy files that either don't exist or are newwe in the destination directory

* `mv`: performs both file moving and file renaming
* `rm`: used to remove files and directories
    * \-r: recursiverly delete directories
    * \-f: ignore nonexistent files and do not prompt

* `ln`: used to create either hard or symbolic links
    * `ln file link`: creates a hard link
    * `ln -s item link`: crates a symbolic link

* Hard links: every file has a single hard link that gives the file its name. The hard link create and additional directory entry for a file
* symbolic links: They create a special type of file that contains a text pointer to the references file or directory
