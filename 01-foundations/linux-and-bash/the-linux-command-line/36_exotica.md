# Group Commands and Subshells

## Group Commands and Subshells

```
(command1; command2; [command3;...])
```

```
{ ls -l; echo "Listing of foo.txt"; cat foo.txt; } > output.txt
```

## Process subtitution

```
while read attr links owner group size date time filename; do
    cat << EOF
        Filename: $filename
        Size: $size
        Owner: $owner
        Group: $group
        Modified: $date $time
        Links: $links
        Attributes: $attr
EOF
done < <(ls -l | tail -n +2)
```
