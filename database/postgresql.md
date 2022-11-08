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