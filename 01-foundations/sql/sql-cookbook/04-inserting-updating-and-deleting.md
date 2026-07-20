# 04. Inserting, Updating and Deleting

## 4.1. Inserting a new record

```
INSERT INTO dept (deptno, dname, loc)
VALUES (50, 'PROGRAMMING', 'BALTIMORE')
```

## 4.2. Inserting default values

```
CREATE TABLE d (id INTEGER DEFAULT 0)
INSERT INTO D VALUES ( DEFAULT )
```

## 4.3. Overriding a default value with NULL

```
CREATE TABLE D ( id INTEGER DEFAULT 0, foo VARCHAR(10) )
INSERT INTO D ( id, foo) values (null, 'Brighten')
```

## 4.4. Copying rows from one table into another

```
INSERT INTO dept_east (deptno, dname, loc)
SELECT deptno, dname, loc
FROM dept
WHERE loc IN ('NEW YORK', 'BOSTON')
```

## 4.5. Copying a table definition

```
CREATE TABLE dept_2
AS
SELECT *
FROM dept
WHERE 1 = 0
```

## 4.6. Inserting into multiple tables at once

```
INSERT ALL
    WHEN loc IN ('NEW YORK', 'BOSTON') THEN
        INTO dept_east (deptno, dname, loc) VALUES (deptno, dname, loc)
    WHEN loc = 'CHICAGO' THEN
        INTO dept_mid (deptno, dname, loc) VALUES (deptno, dname, loc)
    ELSE 
        INTO dept_west (deptno, dname, loc) VALUES (deptno, dname, loc)
    SELECT deptno, dname, loc
    FROM dept 
```

## 4.7. Blocking inserts to certain columns

```
CREATE VIEW new_emps AS
    SELECT empno, ename, job
    FROM emp

INSERT INTO new_emps (empn, ename, job)
VALUES (1, 'Jonathan', 'Editor')
```

## 4.8. Modifying records in a table

```
UPDATE emp
SET sal = sal * 10
WHERE deptno = 20
```

## 4.9. Updating when corresponding rows exist 

```
UPDATE emp
SET sal = sal * 10
WHERE empno IN ( SELECT empno FROM emp_bonus )
```

## 4.10. Updating with values from another table

```
UPDATE emp
SET sal = ns.sal, comm = ns.sal/2
FROM new_sal ns
WHERE ns.deptno = emp.deptno
```

## 4.11. Merging Records

```
MERGE INTO target_table AS target
USING source_table AS source
ON (target.id = source.id)

WHEN MATCHED THEN
    UPDATE SET target.column_name = source.column_name

WHEN NOT MATCHED THEN
    INSERT (id, column_name) 
    VALUES (source.id, source.column_name)

WHEN NOT MATCHED BY SOURCE THEN
    DELETE;
```

## 4.12. Deleting all records from a table

```
DELETE FROM emp
```

## 4.13. Deleting specific records

```
DELETE FROM emp
WHERE deptno = 10
```

## 4.14. Deleting a single record

```
DELETE FROM emp
WHERE empno = 7782
```

## 4.15. Deleting referential integrity violations

```
DELETE FROM emp
WHERE NOT EXISTS (
    SELECT * 
    FROM dept
    WHERE dept.deptno = emp.deptno
)
```

## 4.14. Deleting duplicate records

```
DELETE FROM dupes
WHERE id NOT IN (
    SELECT MIN(id)
    FROM dupes
    GROUP BY name
) 
```

## 4.15. Deleting records referenced from another table

```
DELETE FROM emp
WHERE deptno IN (
    SELECT deptno
    FROM dept_accidents
    GROUP BY deptno
    HAVING COUNT(*) >= 3
)
```
