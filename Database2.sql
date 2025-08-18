-- Active: 1755185527636@@127.0.0.1@3306@ems
SET sql_mode = 'STRICT_ALL_TABLES';

SHOW DATABASES;
CREATE DATABASE ems;
USE ems;

CREATE TABLE department (
    dept_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    hire_date DATE NOT NULL,
    salary INT NOT NULL,
    dept_id INT
);

SHOW TABLES;

INSERT INTO department(dept_id, name)
VALUES
    (1, 'CSE'),
    (2, 'BBA'),
    (3, 'Pharmacy')
;

SELECT * FROM department;
SELECT * FROM employee;

INSERT INTO employee(emp_id,name,hire_date,salary,dept_id)
VALUES
    (101, 'Alice Smith', '2023-01-15', 50000, 1),
    (102, 'Bob Johnson', '2022-05-20', 60000, 2),
    (103, 'Charlie Brown', '2024-03-10', 45000, 1),
    (104, 'David Lee', '2021-11-05', 70000, NULL),
    (105, 'Eva Green', '2023-07-30', 55000, 4)
;

SELECT * FROM employee
ORDER BY hire_date
LIMIT 3;

SELECT * FROM employee
WHERE name LIKE "%e%";

SELECT * FROM employee
WHERE name LIKE "%d L__";

-- -- -- -- Group By and Having
SELECT 
    dept_id,
    SUM(salary),
    COUNT(emp_id)
FROM employee
GROUP BY dept_id;

SELECT 
    dept_id,
    SUM(salary),
    COUNT(emp_id)
FROM employee
GROUP BY dept_id
HAVING SUM(salary)>60000;

SELECT 
    dept_id,
    SUM(salary) AS Total_Salary,
    COUNT(emp_id) AS Num_of_Emp
FROM employee
GROUP BY dept_id
HAVING Total_Salary>60000;

SELECT name,dept_id
FROM employee;

SELECT * FROM employee;
SELECT * FROM department;

-- -- -- -- Join
SELECT
    employee.name,
    department.name
FROM employee
INNER JOIN department
ON employee.dept_id = department.dept_id
;

SELECT
    employee.name,
    department.name
FROM employee
LEFT JOIN department
ON employee.dept_id = department.dept_id
;

SELECT
    employee.name,
    department.name
FROM employee
RIGHT JOIN department
ON employee.dept_id = department.dept_id
;

SELECT
    employee.name,
    department.name
FROM employee
LEFT JOIN department
ON employee.dept_id = department.dept_id
UNION
SELECT
    employee.name,
    department.name
FROM employee
RIGHT JOIN department
ON employee.dept_id = department.dept_id
;

SELECT 
    employee.name,
    employee.salary,
    department.name
FROM employee
LEFT JOIN department
ON employee.dept_id = department.dept_id;

SELECT 
    employee.name,
    employee.salary,
    department.name
FROM employee
LEFT JOIN department
ON employee.dept_id = department.dept_id
WHERE employee.dept_id IS NULL;

SELECT * FROM employee;
SELECT * FROM department;
