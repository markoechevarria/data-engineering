# 32: Positional Parameters

```
echo "
\$# = $#
\$0 = $0
\$1 = $1
\$2 = $2
\$0 = $3
"
```

* `shift`: causes all the paramteres to "move down one" each time it is executed

```
count=1
while [[ $# -gt 0 ]]; do
    echo "Argument $count = $1"
    count=$((count + 1))
    shift
done
```
## Using positional Parameters with shell functions

```
file_info() {
    if [[ -e "$1" ]]; then
        echo -e "\nFile Type:"
        file "$1"
        echo -e "\nFile Status:"
        stat "$1"
    else
        echo "$FUNCNAME: usage: $FUNCNAME file" >&2
        return 1
    fi
}
```

```
usage() {
    echo "$PROGNAME: usage: $PROGNAME [-f file | -i]"
    return
}

interactive=
filename=

while [[ -n "$1" ]]; do
    case "$1" in
        -f | --file)        shift
                            filename="$1"
                            ;;
        -i | --interactive) interactive=1
                            ;;
        -h | --help)        usage
                            exit
                            ;;
        *)                  usage >&2
                            exit 1
                            ;;
    esac
    shift
done
```
