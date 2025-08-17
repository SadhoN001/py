-- Active: 1755185527636@@127.0.0.1@3306@fb
SET sql_mode = 'STRICT_ALL_TABLES'; -- execute that

-- -- -- Common Datatype
-- INT
-- VARCHAR
-- DATE
-- BOOLEAN
-- TIMESTAMP : ( create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP )
-- DECIMAL

CREATE TABLE users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    address TEXT
);
SHOW TABLES;
CREATE Table blogs(
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL
);
SHOW TABLES;
-- table er details dekhte chaile
DESCRIBE users;
DESCRIBE blogs;

SELECT * FROM users;

SELECT * FROM blogs;

INSERT INTO users(age, name)
VALUES(50, "skd");
-- -- error because age not null
-- INSERT INTO users(name, address)
-- VALUES("skd", "ctg")

-- -- error show not name because not null
-- INSERT INTO users(address)
-- VALUES("rangpur")

INSERT INTO users(name, age, address)
VALUES 
    ("Dev", 24, "oxygen"),
    ("kumar", 23, "bayezid")
;

-- -- modify type ,change somethinh
ALTER Table users
MODIFY age INT NOT NULL;
ALTER Table users MODIFY COLUMN addres TEXT NOT NULL;

-- -- add coloum modify
ALTER Table blogs
ADD author_name VARCHAR(100) DEFAULT "Anonymous";

ALTER TABLE user ADD COLUMN category_id INT;
ALTER TABLE user ADD Foreign Key (category_id) REFERENCES Categories(category_id) ON DELETE NULL ON UPDATE CASCADE;
-- -- update values in row
UPDATE users SET age=18 where id=3;
UPDATE users SET address = "bangladesh" WHERE address IS NULL; 

-- -- 1.Select all
SELECT * FROM users;

-- -- 2. Select Specific Column
SELECT name, address FROM users ;
SELECT users.age FROM users;

-- -- 3. Alias
SELECT name AS User_name FROM users;
SELECT u.name FROM users as u;

-- -- 4. Data Filter
SELECT * FROM users where age<20;
SELECT * FROM users where age>0 AND age<40;
SELECT * FROM users where age BETWEEN 0 and 20;
SELECT name, age FROM users WHERE age <20;
SELECT * FROM users WHERE name="skd";

-- -- 5. Aggregate Function(Built in Function)
-- -- (i) Count:
SELECT COUNT(*) FROM users;
SELECT COUNT(*) AS User_count FROM users ;
SELECT COUNT(*) AS User_count FROM users WHERE age <20;
-- -- (ii) Avarage:
SELECT AVG(age) AS Avarage_age FROM users;
SELECT ROUND(AVG(age), 2) AS Average_age FROM users;
SELECT CAST(AVG(age) AS DECIMAL(10,2)) AS Average_age FROM users;
SELECT BIN(AVG(age)) AS Average_age FROM users;
-- -- (iii) Sum:
SELECT SUM(age) AS Total_Salary FROM users;

-- -- 6. In and Not In operator:
SELECT * FROM users WHERE age=23 OR age=25;
SELECT * FROM users WHERE age IN (23,25);
SELECT * FROM users WHERE age NOT IN (23,25);

-- -- 7. Update
UPDATE users SET age=28 WHERE age=21;
ALTER Table users MODIFY COLUMN address TEXT NOT NULL;

SELECT * FROM users WHERE address is not NULL

-- -- 8. Delete
DELETE FROM users WHERE age<10

-- -- ASC and DESC
SELECT * FROM users ORDER BY age ASC;
SELECT * FROM users ORDER BY age DESC;

-- -- limit
SELECT * FROM users LIMIT 5; --5 ta row show korbe
SELECT * FROM users ORDER BY age DESC LIMIT 5; --5 ta row show korbe ulta dike

-- -- like
SELECT * FROM users WHERE name LIKE 'A%';-- A diye suru name show korbe
SELECT * FROM users WHERE name LIKE '%on%';-- A diye suru name show korbe
