-- CREATE Employee(id, emp_id, name, salary, department_id, manager_id, created_at, last_updated_at)
-- id - primary key, auto generated and auto incremented, SEQUENCE(old) and SERIAL(new)
-- emp_id - Unique value which cannot be null
-- name - cannot be null
-- salary - must be 0 or higher, cannot be null
-- department_id - id of the department table, cannot be null
-- manager_id - id of manager, who is also an employee, can be null
-- created_at - automatically entered at time of creation
-- last_updated_at - automatically entered at time of creation as well as on any update in the record

-- CREATE Department(id, name)
-- id - primary key, auto generated, auto incremented, SEQUENCE(old) and SERIAL(new)
-- name - unique and cannot be null

-- create employee table
create table employee(
	id int primary key,
	emp_id varchar(60) not null unique,
	name varchar(60) not null,
	salary int check (salary>=0)
);

-- create department table
create table department(
	id int primary key,
	name varchar(60) not null unique
);

-- add designation_id and manager_id foreign keys to employee table
alter table employee add column designation_id int not null references designation(id);
alter table employee add column manager_id int references employee(id);

-- insert department records


-- insert employee records


-- write a query to get name, department id, number of employees with same name and department


-- write a query to get name, department name, number of employees with same name and department


-- create a view that returns the result of above query


-- create a procedure that takes employee name as argument and returns records / count of records for that employee name


-- create a function to check whether multiple employees exist for a particular employee name bu returning a record if it does otherwise return nothing