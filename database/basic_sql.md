# Basic SQL

```
select <column name>
from <table name>
where <condition>;

SELECT * 
FROM Pets;

SELECT * 
FROM Pets
WHERE PetName = 'Fetch';
```

Advanced actions such as -
creating stored procedures (self contained scripts)
views (pre-made queries)
setting permissions on database objects (such as tables, stored procedures, and views).

--------------------------------
```
CREATE DATABASE PetHotel;

USE PetHotel;

PostgreSQL -> \connect PetHotel or \c PetHotel

CREATE TABLE PetTypes
(
    PetTypeId   int NOT NULL PRIMARY KEY,
    PetType     varchar(60) NOT NULL
);
```

`NOT NULL` columns must contain a value

PetTypeId column the primary key. You can do this in the `CREATE TABLE` statement (like we did here), or you can add one later with an `ALTER TABLE` statement. 
`PRIMARY KEYS` must contain a value. It cannot be `NULL`.
Although primary keys are not required, it’s generally considered good practice to define a primary key on each table.

### FOREIGN KEY
Let’s create two more tables:
```
CREATE TABLE Owners
(
    OwnerId     int NOT NULL PRIMARY KEY,
    FirstName   varchar(60) NOT NULL,
    LastName    varchar(60) NOT NULL,
    Phone       varchar(20) NOT NULL,
    Email       varchar(254)
);

CREATE TABLE Pets
(
    PetId       int NOT NULL PRIMARY KEY,
    PetTypeId   int NOT NULL REFERENCES PetTypes (PetTypeId),
    OwnerId     int NOT NULL REFERENCES Owners (OwnerId),
    PetName     varchar(60) NOT NULL,
    DOB         date NULL
);
```

FOREIGN KEY ensures refential integrity and data integrity.
Prevents bad data from being entered into the database.

### CHECK CONSTRAINTS
In database terms, a CHECK constraint is a type of constraint that checks data before it enters the database.

CHECK constraints help maintain data integrity, because they prevent invalid data entering the database.
```
CREATE TABLE Products( 
    ProductId INTEGER PRIMARY KEY, 
    ProductName, 
    Price 
    CHECK (Price > 0)
);
```

Column-level CHECK constraint might look like this: `CHECK (Price > 0)`
Table-level CHECK constraint might look like this: `CHECK (Price >= Discount)`

### Comment

```
SELECT * FROM Pets; --This is a comment

-- This is a comment
SELECT * FROM Owners;

/*
This is a longer comment so
it's spread across multiple lines
*/
```

### Insert Data

```
INSERT INTO MyTable( Column1, Column2, Column3, ... )
VALUES( Value1, Value2, Value3, ... );

INSERT INTO Pets( PetId, PetTypeId, OwnerId, PetName, DOB )
VALUES( 1, 2, 3, 'Fluffy', '2020-12-20' );

INSERT INTO Pets
VALUES( 1, 2, 3, 'Fluffy', '2020-12-20' );
```

### Select operations

```
SELECT PetId, DOB
FROM Pets
WHERE PetName = 'Fluffy';
```

**Ordering** on single column
```
SELECT PetId, PetName, DOB 
FROM Pets
ORDER BY PetName ASC[or, DESC];
```

Ordering on multiple columns
```
SELECT PetId, PetName, DOB 
FROM Pets
ORDER BY PetName DESC, DOB ASC;
```

**Count**  
You can use the COUNT() aggregate function to count the rows that will be returned in a query.
```
SELECT COUNT(*) AS Count
FROM Pets;
```
You can also specify a particular column to count. The `COUNT()` function **only counts non-NULL results**, so if you specify a column that contains NULL values, those values won’t be counted.

**Grouping**  
```
SELECT 
    PetTypeId, 
    COUNT(PetTypeId) AS Count
FROM Pets
GROUP BY PetTypeId
ORDER BY Count DESC;
```

**Having**
We can use the HAVING clause to `filter the results in the GROUP BY clause`. The HAVING clause returns rows where aggregate values meet specified conditions.
```
SELECT 
    PetTypeId, 
    COUNT(PetTypeId) AS Count
FROM Pets
GROUP BY PetTypeId
HAVING COUNT(PetTypeId) > 2
ORDER BY Count DESC;
```

### Joins
- Inner Join / Natural Join
- Outer Join
  - Left Outer Join
  - Right Outer Join
  - Full Outer Join

```
SELECT 
    PetTypes.PetType,
    COUNT(Pets.PetTypeId) AS Count
FROM Pets 
LEFT JOIN PetTypes 
ON Pets.PetTypeId = PetTypes.PetTypeId
GROUP BY PetTypes.PetType
ORDER BY Count DESC;
+-----------+---------+
| PetType   | Count   |
|-----------+---------|
| Dog       | 4       |
| Cat       | 3       |
| Bird      | 1       |
+-----------+---------+
```

```
SELECT 
    Pets.PetName,
    PetTypes.PetType
FROM Pets 
INNER JOIN PetTypes 
ON Pets.PetTypeId = PetTypes.PetTypeId;
+-----------+-----------+
| PetName   | PetType   |
|-----------+-----------|
| Fluffy    | Cat       |
| Fetch     | Dog       |
| Scratch   | Cat       |
| Wag       | Dog       |
| Tweet     | Bird      |
| Fluffy    | Dog       |
| Bark      | Dog       |
| Meow      | Cat       |
+-----------+-----------+
```

Join more than two tabled together  
```
select dogs.id ID, dogs.gender_code Gender, ddb.BREED_NAME Breed, ddl.CITY_NAME City
from dogs join dim_dog_breed as ddb on dogs.DOG_BREED_ID = ddb.id join dim_dog_location as ddl on dogs.dog_location_id = ddl.id;
```

**Aliases**
An alias allows you to temporarily assign another name to a table or column for the duration of a SELECT query. This can be particularly useful when tables and/or columns have very long or complex names.  

```
SELECT 
    p.PetName AS Pet,
    pt.PetType AS "Pet Type"
FROM PetTypes pt
LEFT JOIN Pets p
ON p.PetTypeId = pt.PetTypeId;
+---------+------------+
| Pet     | Pet Type   |
|---------+------------|
| Tweet   | Bird       |
| Fluffy  | Cat        |
| Scratch | Cat        |
| Meow    | Cat        |
| Fetch   | Dog        |
+---------+------------+

```

**Update Data**

```
UPDATE Owners
SET LastName = 'Stallone'
WHERE OwnerId = 3;
```

**Delete Data**
Deleting some records from the table.  
```
DELETE FROM Owners
WHERE OwnerId = 5;
```

Deleting all records from the table, table remains.  
```
DELETE FROM Owners;
```

**Drop Objects**
```
DROP TABLE Customers;
DROP DATABASE Retail;
```

### SQL Operators

**The Equals (=) Operator**
```
SELECT PetId, PetName, DOB 
FROM Pets
WHERE PetName = 'Fluffy';
```

**The Greater Than (>) Operator**
```
SELECT PetName, DOB 
FROM Pets
WHERE DOB > '2020-01-01';
```
**The Less Than (<) Operator**
**The Greater Than or Equal To (>=) Operator**
**The Less Than or Equal To (<=) Operator**

**The AND Operator**
The AND operator combines two Boolean expressions and returns TRUE when both expressions are TRUE.
```
SELECT PetId, DOB 
FROM Pets
WHERE PetName = 'Fluffy'
AND DOB > '2020-01-01';
```

**The OR Operator**
**The BETWEEN Operator**
```
SELECT
    PetName,
    DOB
FROM Pets
WHERE DOB BETWEEN '2018-01-01' AND '2020-01-01';
+-----------+------------+
| PetName   | DOB        |
|-----------+------------|
| Fetch     | 2019-08-16 |
| Scratch   | 2018-10-01 |
+-----------+------------+
```

**The NOT Operator**
The NOT operator negates a Boolean input (it reverses the value of any Boolean expression). Therefore returns TRUE when the expression is FALSE.

```
SELECT
    PetName,
    DOB
FROM Pets
WHERE DOB NOT BETWEEN '2018-01-01' AND '2020-01-01';
```

**The IN Operator**
The IN operator determines whether a specified value matches any value in a `subquery` or a `list`.  

```
SELECT 
    PetId, 
    PetName, 
    DOB 
FROM Pets
WHERE PetName IN ('Fluffy', 'Bark', 'Wag');
+---------+-----------+------------+
| PetId   | PetName   | DOB        |
|---------+-----------+------------|
| 1       | Fluffy    | 2020-11-20 |
| 4       | Wag       | 2020-03-15 |
| 6       | Fluffy    | 2020-09-17 |
| 7       | Bark      | NULL       |
+---------+-----------+------------+
```

```
SELECT 
    PetTypeId,
    PetType
FROM PetTypes
WHERE PetTypeId IN ( SELECT PetTypeId FROM Pets );

+-------------+-----------+
| PetTypeId   | PetType   |
|-------------+-----------|
| 1           | Bird      |
| 2           | Cat       |
| 3           | Dog       |
+-------------+-----------+

SELECT 
    PetTypeId,
    PetType
FROM PetTypes
WHERE PetTypeId NOT IN ( SELECT PetTypeId FROM Pets );
```

**The + and || and CONCAT String Concatenation Operators**
The `+` and `||` string concatenation operators allows you concatenate strings. String concatenation is the operation of joining character strings end-to-end.  
The `+` operator is supported in `SQL Server`, and the `||` operator is supported in `DB2`, `Oracle`, `PostgreSQL`, `SQLite`.  
If you’re using `MySQL` or `MariaDB`, you’ll need to use the `CONCAT()` function to concatenate strings.
```
SELECT 
    FirstName,
    LastName,
    FirstName + ' ' + LastName AS FullName
FROM Owners;
+-------------+------------+---------------+
| FirstName   | LastName   | FullName      |
|-------------+------------+---------------|
| Homer       | Connery    | Homer Connery |
| Bart        | Pitt       | Bart Pitt     |
| Nancy       | Simpson    | Nancy Simpson |
| Boris       | Trump      | Boris Trump   |
+-------------+------------+---------------+
```

**The LIKE Operator**
- `%`: any number of characters
- `*`: exactly one character
```
SELECT 
    FirstName,
    LastName,
    Email
FROM Owners
WHERE Email LIKE '%.com';

+-------------+------------+-------------------+
| FirstName   | LastName   | Email             |
|-------------+------------+-------------------|
| Homer       | Connery    | homer@example.com |
| Bart        | Pitt       | bart@example.com  |
+-------------+------------+-------------------+
```

```
SELECT 
    FirstName,
    LastName,
    Email
FROM Owners
WHERE Email LIKE 'bart@%.com';
+-------------+------------+------------------+
| FirstName   | LastName   | Email            |
|-------------+------------+------------------|
| Bart        | Pitt       | bart@example.com |
+-------------+------------+------------------+
```

### Views
In SQL, a view is a query that’s saved to the database as a database object (just like a table). The term can also be used to refer to the result set of a stored query. Views are often referred to as `virtual tables`.
```
CREATE VIEW vPetTypeCount AS
SELECT 
    PetTypes.PetType,
    COUNT(Pets.PetTypeId) AS Count
FROM Pets 
LEFT JOIN PetTypes 
ON Pets.PetTypeId = PetTypes.PetTypeId
GROUP BY PetTypes.PetType;

SELECT * FROM vPetTypeCount;

+-----------+---------+
| PetType   | Count   |
|-----------+---------|
| Bird      | 1       |
| Cat       | 3       |
| Dog       | 4       |
+-----------+---------+
```
Any `change to the relations` associated with the view, will be `reflected` while making `query to the view`.  
View is more like an `abstraction` used to hide compelxity of a query, and make it `reusable` and follow `DRY` principle.

The SQL standard **does not allow** the `ORDER BY` clause in any `view definition`. Also, most RDBMSs will raise an error if you try to include an ORDER BY clause.  
```
SELECT * FROM vPetTypeCount
ORDER BY Count DESC;
+-----------+---------+
| PetType   | Count   |
|-----------+---------|
| Dog       | 4       |
| Cat       | 3       |
| Bird      | 1       |
+-----------+---------+
```

### Stored Procedures
A stored procedure is a series of SQL statements compiled and saved to the database. Stored procedures are similar to views in some respects, but very different in other respects.  
```
Stored procedure = View + parameters + conditional programming (if-else) + loops + more ...
```
Pretty much like `functions` in a programming language.  

Different DBMSs have different ways / implementations of procedures.

```
CREATE PROCEDURE uspGetPetById
    @PetId int
AS
    SET NOCOUNT ON;
    SELECT 
        p.PetName, 
        p.DOB, 
        pt.PetType,
        CONCAT(o.FirstName, ' ', o.LastName) AS OwnerName
    FROM Pets p 
    INNER JOIN PetTypes pt 
    ON p.PetTypeId = pt.PetTypeId
    INNER JOIN Owners o 
    ON o.OwnerId = p.OwnerId
    WHERE p.PetId = @PetId;

EXEC uspGetPetById @PetId = 3;

+-----------+------------+-----------+-------------+
| PetName   | DOB        | PetType   | OwnerName   |
|-----------+------------+-----------+-------------|
| Scratch   | 2018-10-01 | Cat       | Bart Pitt   |
+-----------+------------+-----------+-------------+
```

### Trigger
A trigger is a special type of stored procedure that automatically executes when an event occurs in the database server.  
`DML` events are `INSERT`, `UPDATE`, or `DELETE` statements.  
Some DMBSs allow association with both `tables` and `views`, some with tables only.  
`DDL` triggers and `logon` triggers.  
`DDL` events, such as `CREATE`, `ALTER`, and `DROP` statements.  

Stored procedures whose execution is associated with occurence of an event.  

### Transactions
Important part of transactional databases, where data consistency is paramount. A transaction manages a sequence of SQL statements that must be executed as a single unit of work. This is to ensure that the database never contains the results of partial operations.  
When a transaction makes multiple changes to the database, either all the changes succeed when the transaction is committed, or all the changes are undone when the transaction is rolled back.  
A classic example of a transaction is to move money from one bank account to another. You wouldn’t want money to be deducted from the first bank account, but not appear in the second bank account.
```
START TRANSACTION
Debit account 1
Credit account 2
Record transaction in transaction journal
END TRANSACTION 
```

> **MySQL, MariaDB, PostgreSQL**: Explicit transactions start with the `START TRANSACTION` or `BEGIN` statement. `COMMIT` commits the current transaction, making its changes permanent. `ROLLBACK` rolls back the current transaction, canceling its changes.

### Functions
A function is a routine that can take parameters, perform calculations or other actions, and return a result.  

**User-Defined Functions**
For a requirement that isn't catered by inbuilt functions.

**Inbuilt Functions**
Datetime, string formatting, datatype conversion, etc.  

Views and relations are not involved here.