# 02. Sorting query results

## 2.1. Returning query results in a specified order

```
SELECT 
    ename,
    job,
    sal
FROM emp
WHERE deptno = 10
ORDER BY sal ASC
```

## 2.2. Sorting by multiple fields

```
SELECT
    empno,
    deptno,
    sal,
    ename,
FROM emp
ORDER BY deptno, sal desc
```

## 2.3. Sorting by Substrings

```
SELECT
    ename,
    job
FROM emp
ORDER BY substr( job, length(job) - 1 )
```

## 2.4. Sorting mixed alphanumeric data

```
SELECT data
FROM emp
ORDER BY replace(
    data,
    replace(
        translate(
            data,
            '0123456789',
            '#########'
        ),
        '#',
        ''
    ),
    ''
)
```

## 2.5. Dealing with Nulls when sorting

```
SELECT
    ename,
    sal,
    comm
FROM (
    SELECT 
        ename,
        sal,
        comm
    CASE WHEN comm IS NULL THEN 0 ELSE 1 END AS is_null
    FROM emp
)
ORDER BY is_null DESC, comm
```

## 2.6. Sorting on a Data-Dependent Key

```
SELECT
    ename,
    sal,
    job,
    comm
FROM emp
ORDER BY 
    CASE WHEN job = 'SALESMAN' THEN comm ELSE sal END
```
