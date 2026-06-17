

/*The MySQL CREATE DATABASE Statement
The CREATE DATABASE statement is used to create a new SQL database.*/

CREATE DATABASE database_name;


/*Show Databases
Once a database is created, you can check it in the list of databases with the following SQL command:*/
SHOW databases;


/*The DROP DATABASE statement is used to permanently delete an existing SQL database.*/
DROP DATABASE databasename;

/*The CREATE TABLE statement is used to create a new table in a database.*/
CREATE TABLE Persons (
  PersonID int PRIMARY KEY,
  Name  varchar(255) NOT NULL,
  SALARY decimal(2) NOT NULL );


  /*The MySQL DROP TABLE Statement
The DROP TABLE statement is used to permanently delete an existing table in a database.*/

DROP TABLE persons;

/*To prevent an error from occur (if the table does not exists), it is a good practice to add the IF EXISTS clause*/

DROP TABLE IF EXISTS table_name;


/*MySQL TRUNCATE TABLE
The TRUNCATE TABLE statement is used to delete all the records in a table, but it keeps the table structure, columns and constraints.*/

TRUNCATE TABLE persons;




/*MySQL ALTER TABLE Statement
The ALTER TABLE statement is used to add, delete, or modify columns in an existing table.

The ALTER TABLE statement is also used to add and drop various constraints on an existing table.

Common ALTER TABLE operations are:

Add column - Adds a new column to a table
Drop column - Deletes a column in a table
Rename column - Renames a column
Modify column - Changes the data type, size, or constraints of a column
Add constraint - Adds a new constraint
Rename table - Renames a table/*

/*ALTER TABLE - ADD Column
To add a column in a table, use the following syntax:*/

Syntax
ALTER TABLE table_name
ADD column_name datatype;

/*ALTER TABLE - DROP COLUMN
To delete a column in a table, use the following syntax*/

Syntax
ALTER TABLE table_name
DROP COLUMN column_name;












