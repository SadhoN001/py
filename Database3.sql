-- Active: 1755185527636@@127.0.0.1@3306@genex

SHOW DATABASES;
CREATE DATABASE genex;

SHOW TABLES;

-- -- Unique Constrain
CREATE Table user(
    id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    name VARCHAR(100)
);
INSERT INTO user(id,email,name)
VALUES
    (2,"example2@gmail.com", "Example Two");

DROP TABLE user;
SHOW TABLES;

-- default constrain

CREATE Table user(
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(100) UNIQUE,
    name VARCHAR(100),
    country VARCHAR(50) DEFAULT "bangladesh",
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO user(email,name)
VALUES ("example2@gmail.com", "Example Two");
INSERT INTO user(email,name, country)
VALUES ("example3@gmail.com", "Example three", "Nepal");

SELECT * FROM user;

-- -- Check
CREATE TABLE grade(
    id INT PRIMARY KEY AUTO_INCREMENT,
    score INT CHECK(score>=0 AND score<=100)
);

INSERT INTO grade(score) VALUES(50);
INSERT INTO grade(score) VALUES(-5);
INSERT INTO grade(score) VALUES(101);
INSERT INTO grade(score) VALUES(75);
SELECT * FROM grade;

-- -- -- Foreign key constrain
SHOW TABLEs;

CREATE TABLE class(
    id INT PRIMARY KEY
);
SELECT * FROM class;
INSERT INTO class values
    (1), (5), (9), (10);

CREATE TABLE student(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    class_id INT,
    Foreign Key (class_id) REFERENCES class (id)
);
SELECT * FROM student;

INSERT INTO student (name, class_id)
VALUES 
    ("A B", 5),
    ("C D", 9),
    ("E F", 10)
;
INSERT INTO student (name, class_id)
VALUES ("Villan", 2);

SELECT * FROM student;
SELECT * FROM class;
DELETE FROM class WHERE id=5; --  error dibe karon foreign key
DELETE FROM class WHERE id=1; -- 1 id sathe foreign key value store hoi nai tai delete korea jachhe,5 dile hobe na

-- cascade use

DROP TABLE student;
DROP Table class;

CREATE TABLE class(
    id INT PRIMARY KEY
);
SELECT * FROM class;
INSERT INTO class values
    (1), (5), (9), (10);


CREATE TABLE student(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    class_id INT,
    Foreign Key (class_id) REFERENCES class (id)
    ON DELETE CASCADE

);
SELECT * FROM student;
SELECT * FROM class;
INSERT INTO student (name, class_id)
VALUES 
    ("A B", 5),
    ("C D", 9),
    ("E F", 10)
;
INSERT INTO student (name, class_id)
VALUES ("Villan", 2);

DELETE FROM class WHERE id=5; --  error dibe na cascade ase
-- DELETE FROM class WHERE id=1; 

-- correlated subqueries

SHOW TABLES;

DROP TABLE grade;

CREATE TABLE grade(
    id INT PRIMARY KEY AUTO_INCREMENT,
    score FLOAT,
    student_id INT
);
SELECT * FROM grade;
SELECT * FROM student;
INSERT INTO grade(score, student_id )
 VALUES (50,2),(30,3),(90,6),(0,7);

SELECT student_id, score
FROM grade
where score > (
    SELECT AVG(score) FROM grade
);

-- -- common table expression
CREATE TABLE departments(
    id INT PRIMARY KEY ,
    name VARCHAR(50),
    budget DECIMAL(10,2)
);
INSERT INTO departments(id, name, budget)
VALUES
    (1, "HR", 500000.00),
    (2, "IT", 1000000.00),
    (3, "SALES", 750000.00) 
; 
SELECT * FROM departments;
CREATE TABLE employees(
    id INT PRIMARY KEY,
    name VARCHAR(50),
    salary DECIMAL(10,2),
    dep_id INT,
    Foreign Key (dep_id) REFERENCES  departments(id)
);
INSERT INTO employees (id, name, salary, dep_id)
VALUES
    (1, 'Alice', 60000.00, 1),
    (2, 'Bob', 55000.00, 1),
    (3, 'Charlie', 120000.00, 2),
    (4, 'David', 90000.00, 2),
    (5, 'Eve', 80000.00, 2),
    (6, 'Frank', 70000.00, 3),
    (7, 'Grace', 65000.00, 3)
;

SELECT * FROM employees;

WITH dept_avarages AS (
    SELECT dep_id, AVG(salary) as avg_salary
    FROM employees
    GROUP BY dep_id
)
SELECT avg_salary FROM dept_avarages; -- vitorer table tai dhore nisi(virtual table)..oi dhorakei access korte parbo

WITH dept_avarages AS (
    SELECT dep_id, AVG(salary) as avg_salary
    FROM employees
    GROUP BY dep_id
)
SELECT 
    departments.name AS dept_name,
    dept_avarages.avg_salary AS dept_avg_salary
FROM dept_avarages
LEFT JOIN departments
ON dept_avarages.dep_id = departments.id
WHERE dept_avarages.avg_salary > 60000;

-- --index
-- primary index(clustered index) ----------> pk
-- secondary index(Non-clustered index)
SELECT * FROM employees;
SELECT * FROM departments;

CREATE INDEX idx_name ON employees(name);

EXPLAIN
SELECT * FROM employees
WHERE employees.name = "Grace";

EXPLAIN
SELECT * FROM employees
WHERE employees.salary = 65000;

DESCRIBE employees;
