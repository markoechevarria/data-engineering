# 06. Working with strings

## 6.1. Walking a String

```
SELECT substr() AS c
FROM ( SELECT ename FROM emp WHERE ename = 'KING' ) e,
     ( SELECT id AS pos FROM t10 ) iter
WHERE iter.pos <= LENGTH(e.ename)
```

## 6.2. Embedding Quotes Within String Literals

```
SELECT 'g''day mate' qmarks from t1 union all
SELECT 'beavers'' teeth' from t1 union all
SELECT  '''' from t1
```

## 6.3. Counting the Occurrences of a Character in a String

```
SELECT (
    LENGTH ('10,CLARK,MANAGER') - LENGTH ( REPLACE('10,CLARK,MANAGER', ',', '') )
) / LENGTH(',')  AS cnt
FROM t1
```

## 6.4. Removing Unwanted Characters from a String

```
SELECT 
    ename,
    REPLACE ( TRANSLATE( ename, 'aaaaa', 'AEIOU' ), 'a', '' ) AS stripped1
    sal,
    REPLACE ( CAST ( sal AS char(4) ), '0', '' ) AS stripped2
FROM emp
```

## 6.5. Separating Numeric and Character Data

```
SELECT 
    REPLACE(
        TRANSLATE( data, '0123456789', '00000000000'), '0', ''
    ) AS ename,
    CAST(
        REPLACE(
            TRANSLATE ( lower(data), 'abcdefghijklmnopqrstuvwxyz', rpad('z', 26, 'z'),
            'z',
            ''
        ) AS INTEGER
    ) AS sal
FROM (
    SELECT ename || sal 
    AS data
    FROM emp
)
```

## 6.6. Determining whether a string is alphanumeric

```
SELECT data
FROM V
WHERE TRANSLATE (
    lower(data),
    '0123456789abcdefghijklmnopqrstuvwxyz',
    rpad('a', 36, 'a')
) = rpad ('a', LENGHT(data), 'a')
```

## 6.7. Extracting initials from a name

```
SELECT 
    REPLACE (
        REPLACE (
            TRANSLATE (
                REPLACE ('Stewie Griffin', '.', ''), 
                'abcdefghijklmnopqrstuvwxyz', 
                rpad('#',26,'#') 
            ), 
            '#',
            '' 
        ),
        ' ',
        '.' 
    ) ||'.'
FROM t1
```

## 6.8. Ordering by parts of a string

```
SELECT ename
FROM emp
ORDER BY substr(ename, LENGTH(ename) - 1, 2)
```

## 6.10. Creting a delimited list from table rows

```
SELECT
    deptno,
    STRING_AGG( ename ORDER BY empno SEPARATOR, ',') AS emps
FROM emp
GROUP BY deptno
```


