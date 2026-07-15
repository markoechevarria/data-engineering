-- 01. Month with the Highest Total Births

-- Determine the month with the highest total number of births in the playground.us_birth_stats table. 
-- The output should show the month and the total number of births.

SELECT 
    month, 
    SUM(births) AS total_births
FROM playground.us_birth_stats 
GROUP BY month 
HAVING COUNT(1) = 465
ORDER BY total_births DESC
LIMIT 1

-- 02. Find Viewers with Multiple Article Views in a Day	
-- Using the table playground.views, write a SQL query to identify all viewers who viewed more than one article on the same day. 
-- The table includes columns viewer_id (the ID of the viewer), article_id (the ID of the article viewed), 
-- and view_date (the date of the view). The result should contain a single column named viewer_id, 
-- listing each viewer who meets the criteria without duplicates, and should be sorted in ascending order of viewer_id.

SELECT 
  viewer_id, 
  COUNT(DISTINCT article_id) AS times
FROM playground.views 
GROUP BY view_date, viewer_id
HAVING 
  COUNT(DISTINCT article_id) >= 2

-- 03. Total Number of Births Per Year	
-- Write a SQL query to calculate the total number of births recorded for 
-- each year in the playground.us_birth_stats table. Order the results by year.

SELECT 
  year, 
  SUM(births) AS total_births
FROM playground.us_birth_stats 
GROUP BY year 
ORDER BY year

-- 04. Cars with Above Average Engine Size	
-- Using the table playground.automobile, Create a SQL query to identify cars that have an engine size 
-- above the average across all cars in the dataset. The result should include the brand, 
-- fuel_type, and engine size, ordered by engine size in descending order and then brand_name in asc order.

SELECT 
  brand_name,
  fuel_type,
  engine_size
FROM playground.automobile 
WHERE engine_size > (
  SELECT AVG(engine_size)
  FROM playground.automobile
)
ORDER BY 
  engine_size DESC, 
  brand_name ASC

-- 05. Check Test Answers
-- Create a SQL query to evaluate test answers stored in a table named playground.answers 
-- with columns id (unique question ID), correct_answer (string), and given_answer (which can be NULL). 
-- Return a table with columns id and checks, where checks is "no answer" if given_answer is NULL,
-- "correct" if given_answer matches correct_answer, and "incorrect" otherwise. Order the results by id.

SELECT 
  id,
  CASE 
    WHEN given_answer IS NULL THEN 'no answer'
    WHEN correct_answer = given_answer THEN 'correct'
    ELSE 'incorrect'
  END AS checks
FROM playground.answers

-- 06. Average Number of Births by Day of the Week
-- Create a SQL query that finds the average number of births for each day of the week across all years 
-- in the playground.us_birth_stats table. Cast the average as an integer. Order the results by the day of the week.

SELECT 
  day_of_week, 
  CAST( AVG(births) AS INT ) AS average_births
FROM playground.us_birth_stats 
GROUP BY day_of_week
ORDER BY day_of_week

-- 07. Identifying Empty Departments
 
-- Given two tables, playground.employees and playground.departments, with employees containing id, full_name, 
-- and department, and departments containing id (unique department ID) and dep_name (department name), 
-- write a SQL query to build a table with one column, dep_name. This table should list all the departments 
-- that currently have no employees, sorted by the department id.

SELECT d.dep_name
FROM playground.departments d
LEFT JOIN playground.employees e
ON e.department = d.id
WHERE e.id IS NULL

SELECT dep_name
FROM playground.departments 
WHERE id NOT IN (
  SELECT DISTINCT department
  FROM playground.employees
)

-- 08. Filtering Students in Active Clubs
-- Given tables clubs (id: unique club id, name: club name) and students (id: unique student id, name: student name, 
-- club_id: club's id), return a list from the students table for those who are in clubs that still exist 
-- in the clubs table. The result should have three columns (id, name, club_id) and be sorted by students' ids (id) 
-- and include only those students whose club_id matches an id in the clubs table.

SELECT 
  id,
  name,
  club_id
FROM playground.students
WHERE club_id IN (
  SELECT DISTINCT id
  FROM playground.clubs
)

-- 09. Identifying the Bank Robber
-- Using table playground.suspect, filter out suspects who cannot be the bank robber based on the following clues: 
-- the robber is not taller than 170cm, and their name matches the pattern "B. Gre?n" where the first letter of 
-- the name is "B" or "b" and the surname is similar to "Green" but with the fourth letter being unreadable and 
-- potentially any character. The match should be case-insensitive. For each suspect that fits these criteria, 
-- select their id, name, and surname. Order the results by suspect id in ascending order.

SELECT 
  id,
  name,
  surname
FROM playground.suspect
WHERE 
  height <= 170 AND
  LOWER(name) LIKE 'b%' AND
  LOWER(surname) LIKE '%gre_n'

-- 10. Determining the Order of Succession
-- Given a table Successors with columns: name, birthday, and gender, write a SQL query to list the names of 
-- the King's children in order of their succession to the throne and their birthday("name", "birthday"). 
-- Succession is based on age seniority. Prefix the name with "King" for males and "Queen" for females. 
-- The result should be sorted by birthday in ascending order to determine the succession order.

SELECT 
  CASE 
    WHEN gender = 'M' THEN CONCAT('', name)
    WHEN gender = 'F' THEN CONCAT('', name)
  END AS name,
  birthday
FROM playground.successors
ORDER BY birthday

-- 11. 