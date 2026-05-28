# 24. Writing your first script

* A shell script is a file containing a series of commands

```
#!/bin/bash
# This is our first script.
echo 'Hello World!'
```

* Scripts should be executables, use `chmod` for it
* Scripts can be written using multiple lines.

```
find playground \
    \( \
        -type f \
        -not -perm 0600 \
        -exec chmod 0600 '{}' ';' \
    \) \
    -or \
    \( \
        -type d \
        -not -perm 0700 \
        -exec chmod 0700 '{}' ';' \
    \)
```
