# 28. Reading Keyboard Input

* read - Read values from standard input

`read [-options] [variable...]`: used to read a single file of standard input
```
echo -n "Please entre an integer ->"
read var1 var2 var3 var4
```
* `-a`: assign the input to array
* `-d delimiter`: the first character in the string *delimiter* is used to indicate the end of input
* `-e`: user Readline to handle input
* `-i string`: use *string* as a default reply
* `-n num`: read *num* chracters of input
* `-p prompt`: display a prompt for input using the string prompt
* `-r`: raw mode, do not interpret backslash characters as escapes
* `-s`: silent mode, do not echo chracters to the display as they are typed
* `-t seconds`: terminate input after *seconds*
* `-u fd`: use input from the file descriptor *fd* rather than standard input

## IFS

```
FILE=/etc/passwd
read -p "Enter a username > " user_name
file_info="$(grep "^$user_name:" $FILE)"

if [ -n "$file_info" ]; then
    IFS=":" read user pw uid gid name home shell <<< "$file_info"
    echo "User = '$userr'"
else
    echo "No such user '$user_name'" >&2
    exit 1
fi
```




