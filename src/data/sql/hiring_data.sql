-- Crear el keyspace hired_data
CREATE KEYSPACE hired_data WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

-- Create table departments
CREATE TABLE departments (
    id INT PRIMARY KEY,
    department TEXT
);

-- Create table jobs
CREATE TABLE jobs (
    id INT PRIMARY KEY,
    job TEXT
);

-- Create table hired_employes
CREATE TABLE hired_employees (
    id INT,
    name TEXT,
    datetime TIMESTAMP,
    department_id INT,
    job_id INT,
    PRIMARY KEY (id)
) WITH CLUSTERING ORDER BY (datetime DESC);
