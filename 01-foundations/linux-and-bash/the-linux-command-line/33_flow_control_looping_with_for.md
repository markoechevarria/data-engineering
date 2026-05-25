# 33. Flow control: Looping with for

```
for variables [in words]; do
    commands
done
```

```
for i in distros*.txt; do
    if [[ -e "$i" ]]; then
        echo "$i"
    fi
done
```

## for: C language form

```
for (( expression1; expression2; expression3 )); do
    commands
done
```
