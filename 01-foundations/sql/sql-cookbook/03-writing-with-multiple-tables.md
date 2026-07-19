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
