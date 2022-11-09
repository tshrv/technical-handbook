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

### Auto-populating timestamp
- `created_at` set to current timestamp on creation
- `last_updated_at` set to current timestamp on creation as well as on every update on table.
```sql
create table employee(
	id serial primary key,
	name varchar(60) not null,
	created_at timestamp default now(),
	last_updated_at timestamp default now()
);
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

### Trigger
- A PostgreSQL trigger is a function invoked automatically whenever an event associated with a table occurs. An event could be any of the following: `INSERT`, `UPDATE`, `DELETE` or `TRUNCATE`.
- A trigger is a special **user-defined function** associated with a **table**.
- Two main types of triggers: `row-level` and `statement-level` triggers. The differences between the two kinds are how many times the trigger is invoked and at what time.
- Create a trigger function using `CREATE FUNCTION` statement.
- Bind the trigger function to a table by using `CREATE TRIGGER` statement.

A trigger function is similar to a regular user-defined function. However, a trigger function does not take any arguments and has a return value with the type `trigger`.

```sql
CREATE FUNCTION trigger_function() 
   RETURNS TRIGGER 
   LANGUAGE PLPGSQL
AS $$
BEGIN
   -- trigger logic
END;
$$
```

- A trigger function receives data about its calling environment through a special structure called `TriggerData` which contains a set of local variables.
- `OLD` and `NEW` represent the states of the row in the table before or after the triggering event.
- Also provides other local variables preceded by `TG_` such as `TG_WHEN`, and `TG_TABLE_NAME`.
- Once you define a trigger function, you can **bind** it to one or more trigger events such as `INSERT`, `UPDATE`, and `DELETE`.

```sql
CREATE TRIGGER trigger_name 
   {BEFORE | AFTER} { event }
   ON table_name
   [FOR [EACH] { ROW | STATEMENT }]
       EXECUTE PROCEDURE trigger_function
```
- Row-level trigger that is specified by the `FOR EACH ROW` clause.
- Statement-level trigger that is specified by the `FOR EACH STATEMENT` clause.