# 01. Retrieving Records

## 1.1. Retrieving all rows and columns from a table

```
SELECT * 
FROM emp
```

## 1.2. Retrieving a subset of rows from a table

```
SELECT *
FROM emp
WHERE deptno = 10
```

## 1.3. Finding rows that satisfy multiple conditions

```
SELECT *
FROM emp
WHERE deptno = 10
    OR comm IS NOT NULL
    OR sal <= 2000 AND deptno = 20
```

## 1.4. Retrieving a subset of columns from a table

```
SELECT
    ename, 
    deptno, 
    sal
FROM emp
```

## 1.5. Providing meaningful names for columns

```
SELECT 
    sal AS salary,
    comm AS commision
FROM emp
```

## 1.6. Referencing an Aliased column in the WHERE clause

```
SELECT *
FROM (
    SELECT 
        sal AS salary,
        comm AS commision
    FROM emp
)
WHERE salary < 5000
```

* Standard SQL first execute FROM, then WHERE and finally SELECT, certain engine databases allow use alias without requiering to use a subquery

## 1.7. Concatening Column Values

```
SELECT 
    enam || 'WORKS AS A ' || job AS msg
FROM emp
WHERE deptno = 10
```

## 1.8. Using conditional logic in a SELECT statement

```
SELECT 
    ename,
    sal,
    CASE 
        WHEN sal <= 2000 THEN 'UNDERPAID'
        WHEN sal >= 4000 THEN 'OVERPAID'
        ELSE 'OK'
    END AS status
FROM emp
```

## 1.9. Limiting the Number of Rows returned

```
SELECT *
FROM emp
LIMIT 5
```

## 1.10. Returning n Random Records from a Table

```
SELECT
    ename,
    job
FROM emp
ORDER BY random()
LIMIT 5
```

* The ORDER BY clause can accept a function's return value and use it to change the order of the result set, also can accept numeric constants, they referring to the to the ordinal positionin the SELECT list

## 1.11. Finding Null values

```
SELECT *
FROM emp
WHERE comm IS NULL
```

## 1.12. Transforming Nulls into Real Values

```
SELECT COALESCE(comm, 0)
FROM emp
```

## 1.13. Searching for Patterns

```
SELECT
    ename,
    job
FROM emp
WHERE 
    depno IN (10, 20) AND
    ( ename LIKE '%I%' OR job LIKE '%ER' )
```
