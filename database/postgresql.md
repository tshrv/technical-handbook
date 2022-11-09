# PostgreSQL

- Create database
- Create table1
- alter / add column
- update column
- Create table two
- add foreign key to table 1
- create indexes for both tables


## Sequence
```sql
CREATE SEQUENCE [ IF NOT EXISTS ] sequence_name
    [ AS { SMALLINT | INT | BIGINT } ]
    [ INCREMENT [ BY ] increment ]
    [ MINVALUE minvalue | NO MINVALUE ] 
    [ MAXVALUE maxvalue | NO MAXVALUE ]
    [ START [ WITH ] start ] 
    [ CACHE cache ] 
    [ [ NO ] CYCLE ]
    [ OWNED BY { table_name.column_name | NONE } ]

CREATE SEQUENCE mysequence
INCREMENT 5
START 100;

SELECT nextval('mysequence');

INSERT INTO 
    order_details(order_id, item_id, item_text, price)
VALUES
    (100, nextval('mysequence'),'DVD Player',100),
    (100, nextval('mysequence'),'Android TV',550),
    (100, nextval('mysequence'),'Speaker',250);

drop sequence mysequence;
```

### Creating and querying from a view
```sql
create view vfilmgr as
select film_id fid
from inventory
group by film_id
having count(inventory_id)>7;

select count(*) from vfilmgr;
```

### Creating and calling a procedure in psql
```sql
drop procedure if exists update_actor_last_name;
create procedure update_actor_last_name(
	target_actor_id int,
	new_last_name varchar
)
language plpgsql
as $$
BEGIN
	update actor
	set last_name=new_last_name
	where actor.actor_id=target_actor_id;
END$$;
```

### Date and time
```sql
select current_date, current_time, current_timestamp;
```

## Alter
### Rename
```sql
alter table employee rename column designation_id to department_id;
```

### Add column
```sql
alter table employee add column designation_id int not null references department(id);
```

### Auto-incrementing Column
**Sequence**

```sql
create sequence department_id_sequence
start 1
increment 1;

create table department(
    id int primary key default nextval('department_id_sequence'),
    name varchar(60) not null unique
);
insert into department(name) values ('Digital Transformations');
insert into department(name) values ('Digital Solutions');
insert into department(name) values ('Cloud Modernization');
```

**Serial**
```sql
create table employee(
	id serial primary key,
	emp_id varchar(60) not null unique,
	name varchar(60) not null,
	salary int check (salary>=0)
);
```

### Add Foreign Key
**While Creation**
```sql
create table employee(
	id serial primary key,
	emp_id varchar(60) not null unique,
	name varchar(60) not null,
	salary int check (salary>=0),
    department_id int,
    foreign key (department_id) references department (id)
);
```

**Post Creation**
```sql
alter table employee add column department_id int not null references department(id);
```

### Insert Multiple Rows
```sql
insert into employee
(emp_id, name, salary, department_id)
values
('tushar@epam.com', 'Tushar', 10, 1),
('tushar+1@epam.com', 'Tushar', 20, 1),
('tushar+2@epam.com', 'Tushar', 30, 1),
('ayush@epam.com', 'Ayush', 13, 3);
```

### Update Records
```sql
update employee
set 
manager_id=12
where
id in (13, 14, 15);
```

### View
```sql
create view similar_employees_view;
as
select em.name EmployeeName, dt.name DepartmentName, count(em.name) NumberOfEmployees
from employee em join department dt on em.department_id = dt.id
group by em.name, dt.name
having count(em.name) > 1;

select * from similar_employees_view;
```

### Procedure Vs Function
A drawback of user-defined functions is that they cannot execute transactions. In other words, inside a user-defined function, you cannot start a transaction, and commit or rollback it.

### Function
**Format**
```sql
create [or replace] function function_name(param_list)
   returns return_type 
   language plpgsql
  as
$$
declare 
-- variable declaration
begin
 -- logic
end
$$;
```

**Example**
```sql
create function get_film_count(len_from int, len_to int)
returns int
language plpgsql
as
$$
declare
   film_count integer;
begin
   select count(*) 
   into film_count
   from film
   where length between len_from and len_to;
   
   return film_count;
end;
$$;
```
- A function can have zero or many parameters.
- Place a block in the dollar-quoted string constant. You can place a block that contains the declaration and logic of the function.
- Use the `select into` statement to select the number of films whose length are between len_from and len_to and assign the result to the film_count variable. At the end of the block, use the return statement to return the film_count.

**Calling a procedure - positional notation**
```sql
select get_film_count(40,90);
```

**Calling a procedure - named notation**
```sql
select get_film_count(
    len_from => 40, 
     len_to => 90
);
```

### Procedure
```sql
create [or replace] procedure procedure_name(parameter_list)
language plpgsql
as $$
declare
-- variable declaration
begin
-- stored procedure body
end; $$
```

- Does not return a value. You cannot `return expression;`
- Can use the return statement without the expression to stop the stored procedure immediately, `return;`
- If you want to return a value from a stored procedure, you can use parameters with the `inout`(passed in as arguments, updated in procedure and returned in the end) mode.