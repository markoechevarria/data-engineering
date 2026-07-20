# 11. Advanced Searching

## 11.1 Pagination through a result set

```
SELECT sal
FROM (
    SELECT 
        ROW_NUMBER() OVER (ORDER BY sal) AS rn,
        sal
    FROM emp
)
WHERE rn BETWEEN 1 AND 5
```

## 11.2. Skipping n Rows from a table

```
SELECT ename
FROM (
    SELECT 
        ROW_NUMBER() OVER (ORDER BY ename) rn,
        ename
    FROM emp     
)
WHERE mod(rn, 2) = 1
```

## 11.3. Incorporating OR logic when using outer joins

```
SELECT
    e.ename,
    d.deptno,
    d.dname,
    d.loc
FROM dept d
LEFT JOIN emp e
ON (d.deptno = e.deptno AND ( e.deptno = 10 OR e.deptno = 20) )
ORDER BY 2
```

## 11.4. Determining Which Rows Are Reciprocals

```
SELECT 
    DISTINCT v1.*
FROM V v1, V v2
WHERE
    v1.test1 = v2.test2 AND
    v1.test2 = v2.test1 AND
    v1.test1 <= v1.test2
```

## 11.5. Selecting the Top n Records

```
SELECT
    ename,
    sal
FROM (
    SELECT 
        ename,
        sal,
        DENSE_RANK() OVER (ORDER BY sal DESC) dr
    FROM emp
)
WHERE dr <= 5
```

## 11.6. Finding Records with the Highest and Lowest Values

```
SELECT 
    ename
FROM (
    SELECT
        ename,
        sal,
        MIN(sal) OVER() min_sal,
        MAX(sal) OVER() max_sal
    FROM emp
)
WHERE sal IN (min_sal, max_sal)
```

## 11.7. Investigating Future Rows

```
SELECT 
    ename,
    sal,
    hiredate
FROM (
    SELECT 
        ename,
        sal,
        hiredate
    LEAD(sal) OVER(ORDER BY hiredate) next_sal
    FROM emp
)
WHERE sal < next_sal
```

## 11.8. Shifting Row values

```
SELECT 
    ename,
    sal,
    COALESCE( LEAD(sal) OVER(ORDER BY sal), MIN(sal) OVER() ) forward,
    COALESCE( LAG(sal) OVER(ORDER BY sal), MAX(sal) OVER() ) rewind
FROM emp
```

## 11.9. Ranking Results

```
SELECT 
    DENSE_RANK() OVER ( ORDER BY sal ) rnk,
    sal
FROM emp
```

## 11.10. Suppressing Duplicates

```
SELECT 
    job,
FROM (
    SELECT
        job,
        ROW_NUMBER() OVER(PARTITION BY job ORDER BY job) rn
    FROM emp
)
WHERE rn = 1
```

## 11.11. Finding Knight Values

```
SELECT
    deptno,
    ename,
    sal,
    hiredate,
    MAX(latest_sal) OVER(PARTITION BY deptno) latest_sal
FROM (
    SELECT
        deptno,
        ename,
        sal,
        hiredate,
        CASE
            WHEN hiredate = MAX(hiredate) OVER(PARTITION BY deptno)
            THEN sal ELSE 0
        END latest_sal
    FROM emp
)
ORDER BY 1, 4 DESC
```

## 11.12. Generating Simple Forecasts 

SELECT 
    id,
    order_date,
    process_date,
    CASE WHEN gs.n >= 2
         THEN process_date + 1
         ELSE null
    CASE WHEN gs.n = 3
         THEN process_date + 2
         ELSE null
    END AS shipped

FROM (
    SELECT 
        gs.id,
        currend_date + gs.id AS order_date,
        currend_date + gs.id + 2 AS process_date
    FROM generate_series(1,3) gs (id)
) orders,
generate_series(1,3) gs(n)
