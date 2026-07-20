# 03. Working with multiple tables

## 3.1. Stacking one rowset atop another

```
SELECT 
    ename AS ename_and_dname,
    deptno
FROM emp
WHERE deptno = 10

UNION ALL

SELECT '---------', null
FROM t1

UNION ALL

SELECT
    dname,
    deptno
FROM deptno
```

## 3.2. Combining related rows

```
SELECT
    e.ename,
    d.loc
FROM emp e, dept d
WHERE e.deptno = d.deptno
    AND e.deptno = 10
```

## 3.3. Finding rows in common between two tables 

```

CREATE VIEW V AS
    SELECT 
        ename,
        job,
        sal
    FROM emp
    WHERE job = 'CLERK'

SELECT
    e.empno,
    e.ename,
    e.job,
    e.sal,
    e.deptno
FROM emp e, V
WHERE e.ename = v.ename
    AND e.job = v.job
    AND e.sal = v.sal
```

## 3.4 Retrieving values from one table that do not exist in another. 

```
SELECT deptno
FROM dept

EXCEPT 

SELECT deptno
FROM emp
```

## 3.5. Retrieving rows from one table that do not correspond to rows in another

```
SELECT d.*
FROM dept d
LEFT JOIN emp e
    ON d.deptno = e.deptno 
WHERE e.deptno IS NULL
```

## 3.6. Adding joins to a query without interfering with other joins

```
SELECT
    e.ename,
    d.loc,
    eb.received
FROM emp e
JOIN dept d
    ON e.deptno = d.deptno
LEFT JOIN emp_bonus eb
    ON e.empno = eb.empno
ORDER BY 2
```

## 3.7. Determining whether two talbes have the same data

* Find rows in table EMP that do not exist in view V
* Combine (UNION ALL) those rows with rows from view V that do not exist in table EMP

## 3.8. Identifying and avoiding cartesian products

```
SELECT
    e.ename,
    d.loc
FROM emp e, dept d
WHERE e.deptno = 10 AND deptno = e.deptno
```

## 3.9. Performing Joins when using aggregates

```
SELECT
    d.deptno,
    d.total_sal,
    sum(
        e.sale * CASE WHEN eb.type = 1 THEN .1
                      WHEN eb.type = 2 THEN .2
                      ELSE .3 END
    ) AS total_bonus
FROM emp e,
     emp_bonus eb,
     (
        SELECT
            deptno,
            sum(sal) AS total_sal
        FROM emp
        WHERE deptno = 10
        GROUP BY deptno 
    ) d
WHERE e.deptno = d.deptno AND e.empno = eb.empno
GROUP BY d.deptno, d.total_sal
```

## 3.10. Performing Outer Joins when using aggregates

```
SELECT 
    deptno,
    SUM( DISTINCT sal ) AS total_sal,
    SUM( bonus ) AS total_bonus
FROM (
    SELECT e.empno,
           e.ename,
           e.sal,
           e.deptno,
           e.sal * CASE ...
    FROM emp e
    LEFT JOIN emp_bonus eb
    ON e.empno = eb.empno 
    WHEER e.deptno = 10
)
GROUP BY deptno
```

## 3.11. Returning missing data from multiple tables

```
SELECT 
    d.deptno,
    d.dname,
    e.ename
FROM dept d
FULL JOIN emp e
ON e.deptno = e.deptno
```

## 3.12. Using NULLS in operations and comparisons

```
SELECT
    ename,
    comm
FROM emp
WHERE COALESCE(comm, 0) < ( SELECT comm FROM emp WHERE ename = 'WARD')
```

