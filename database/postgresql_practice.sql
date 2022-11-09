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
	id serial primary key,
	emp_id varchar(60) not null unique,
	name varchar(60) not null,
	salary int check (salary>=0)
);

-- create department table
-- primary key using sequence
create sequence department_id_sequence
start 1
increment 1;

create table department(
	id int primary key default nextval('department_id_sequence'),
	name varchar(60) not null unique
);

-- add designation_id and manager_id foreign keys to employee table
alter table employee add column designation_id int not null references designation(id);
alter table employee add column manager_id int references employee(id);

-- add created_at and last_updated_at column which are auto populated

-- insert department records
insert into department (name)
values
('Digital Transformations'),
('Digital Solutions'),
('Cloud Modernization');

-- insert employee records
insert into employee
(emp_id, name, salary, department_id)
values
('tushar@epam.com', 'Tushar', 10, 1),
('tushar+1@epam.com', 'Tushar', 20, 1),
('tushar+2@epam.com', 'Tushar', 30, 1),
('ayush@epam.com', 'Ayush', 13, 3);

-- write a query to get name, department id, number of employees with same name and department
select em.name, em.department_id, count(em.department_id)
from employee em
group by em.name, em.department_id
having count(em.department_id) > 1;

-- write a query to get name, department name, number of employees with same name and department
select em.name EmployeeName, dt.name DepartmentName, count(em.name) NumberOfEmployees
from employee em join department dt on em.department_id = dt.id
group by em.name, dt.name
having count(em.name) > 1;

-- create a view that returns the result of above query
create view similar_employees
as
select em.name EmployeeName, dt.name DepartmentName, count(em.name) NumberOfEmployees
from employee em join department dt on em.department_id = dt.id
group by em.name, dt.name
having count(em.name) > 1;

-- create a procedure that takes employee name as argument and returns records / count of records for that employee name


-- create a function to check whether multiple employees exist for a particular employee name, returning an int or a boolean
create or replace function duplicate_employees_exist(emp_name varchar)
returns bool
language plpgsql
as
$$
declare
	duplicates_employees_count int;
begin
	select count(*) into duplicates_employees_count
	from similar_employees_view
	where employeename = emp_name;
	
	return duplicates_employees_count;
end;
$$;
select duplicate_employees_exist('Tushar');

-- create a function to check whether multiple employees exist for a particular employee name, returning a record if it does otherwise return nothing
drop function if exists duplicate_employees_exist;
create or replace function get_duplicate_employees(emp_name varchar)
returns table (employeename varchar, departmentname varchar, numberofemployees bigint)
language plpgsql
as
$$
declare
-- 	no variable declaration required
begin
	return query
		select sev.employeename, sev.departmentname, sev.numberofemployees
		from similar_employees_view sev
		where sev.employeename = emp_name;
end;
$$;

select * from get_duplicate_employees('Tushar');