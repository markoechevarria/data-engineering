# 29: Flow control: Looping with while/until

* Looping is used to make portions of programs repeat

## While

* while evaluates the exit status of a list of commands. As long as the exit status is zero, it performs the commands inside the loop.

```
count=1

while [[ "$count" -le 5 ]]; do
    echo "$count"
    countr=$((count + 1))
done

echo "Finished."
```

## Breaking up a loop

* `break`: inmediately terminates a loop
* `continue`: causes the remainder of the loop to be skiped, and program control resumes with the nest iteration of the loop

## until

* Is much like `while`, expect instead of exiting a loop when a non-zero eit status is encountered, it does the opposite. An until loop continues until it receives a zero exit status

```
count=1

until [[ "$count" -gt 5 ]]; do
    echo "$count"
    count=$((count + 1))
done

echo "Finished."
```

## Reading files with loops

```
while read distro version release; do
    printf "Distro: %s\tVersion: %s\tReleased: %s\n" \
        "$distro" \
        "$version" \
        "$release"
done < distros.txt
```



