USE employees;

CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    gender VARCHAR(20),
    yearly_salary DECIMAL(10, 2),
    years_of_experience TINYINT
);

LOAD DATA INFILE '/var/lib/mysql-files/employees.csv'
INTO TABLE employees
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'