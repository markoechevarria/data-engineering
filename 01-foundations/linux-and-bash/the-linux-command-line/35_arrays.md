# 35. Arrays

* Arrays are variables that hold more than one value at a time

```
a[1]=foo
echo ${a[1}
```

```
name[subscript]=value
name=(value1 value2 ...)
```

```
usage() {
    echo "usage: ${0##*/} directory" >&2
}

if [[ ! -d "$1" ]]; then
    usage
    exit
fi

for i in {0..23}; do hours[i]=0; done

for i in $(stat -c %y "$1"/* | cut -c 12-13); do
    j="${i#0}"
    ((++hours[j]))
    ((++count))
done

echo -e "Hour\tFiles\tHour\tFiles"
echo -e "----\t-----\t----\t-----"
for i in {0..11}; do
    j=$((i + 12))
    printf "%02d\t%d\t%02d\t%d\n" \
        "$i" \
        "${hours[i]}" \
        "$j" \
        "${hours[j]}"
done
printf "\nTotal files = %d\n" $count
```

## Outputting the Entire Contents of an Array

```
animals=("a dog" "a cat" "a fish")
for i in ${animals[@]}; do echo $i; done
```

## Determining the Number of Array elements

```
echo ${#a[@]}
echo ${#a[100]}
```

## Adding elements to the end of an array

```
foo=(a b c)
foo+=(d e f)
```

## Sorting an array

```
a=(f e d c b a)
a_sorted=($(for i in "${a[@]}"; do echo $i; done | sort))
```

## Deleting an array

```
foo=(a b c d e f)
echo ${foo[@]}
unset 'foo[2]'
unset foo
```
