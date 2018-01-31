# SQL

![Comic](https://imgs.xkcd.com/comics/exploits_of_a_mom.png "Her daughter is named Help I'm trapped in a driver's license factory.")

_XKCD comic featuring SQL humor. Hopefully, by the end of this essay, you will understand the joke! ([Link](https://xkcd.com/327/))_

SQL (["Structured Query Language"](https://en.wikipedia.org/wiki/SQL)) is a language for querying, manipulating, inserting, and deleting data within relational databases. Even though, SQL is [almost 50 years old](https://dl.acm.org/citation.cfm?doid=362384.362685), [many relational database systems](https://en.wikipedia.org/wiki/List_of_relational_database_management_systems) still used today, handle interactions through SQL statements. In the sections below, I will show how SQL can be used on large data sets, to both aggregate features of several rows, and look at single rows in detail. 

### Syntax
<!--img src="https://user-images.githubusercontent.com/6633242/35548378-3f09f0be-053c-11e8-9473-cad2b033350d.png" width="70%" title="Example Database"-->

[Relational databases](https://en.wikipedia.org/wiki/Relational_database) are those in which rows ("records") that contain common columns ("attributes") are stored within tables ("relations"). Using the language of records, attributes, and relations, operations on relational databases using SQL statements generally follow a [format](https://en.wikipedia.org/wiki/SQL_syntax) that looks something like:
```SQL
<SELECT/INSERT/UPDATE/DELETE> ... records ... 
	<FROM/INTO/SET> ... relation ... 
		<VALUES/WHERE> ... attributes ...
``` 

Let's take a deeper dive into four of the common SQL operations:

#### [SELECT](https://en.wikipedia.org/wiki/Select_(SQL))

In order to look at all of the records, and all of their attributes, from a particular table (`relation`), your SQL statement will look something like:
```SQL
SELECT * FROM relation
``` 

If you have a huge dataset, it would be wise to tack a LIMIT clause to the above statment. For example:
```SQL
SELECT * FROM relation LIMIT 10
```
returns the first 10 records from your query results (analogous of `head` from Unix, on a database).

To query for a particular attribute (`index`), again over all records:
```SQL
SELECT index FROM relation
``` 

If you'd like to examine a single record (here, the first), with all of its attributes, you will use a [WHERE](https://en.wikipedia.org/wiki/Where_(SQL)) clause:
```SQL
SELECT * FROM relation WHERE index = 1
```
(There are [many other operators](https://en.wikipedia.org/wiki/SQL_syntax#Operators), like `=`, that can be used within SQL statements.)

There are also many additional optional clauses one can specify to further limit, aggregate or sort the results of a SELECT. Some of these include:

- GROUP BY: aggregate results by a particular attribute of your records (e.g. group all sales belonging to a single department)
- [HAVING](https://en.wikipedia.org/wiki/Having_(SQL)): essentially a WHERE clause applied to groups (e.g. filter all sales belonging to a single department which exceed $1,000)
- [ORDER BY](https://en.wikipedia.org/wiki/Order_by): sort results (in ascending order, by default) based on a specific attribute (e.g. return sales sorted by transaction date)

These clauses can be particularly helpful when using [aggregate functions](https://en.wikipedia.org/wiki/Aggregate_function).

Hopefully, after just this discussion of SQL's SELECT statement, I have conveyed some of the power behind SQL - primarily, its ability to generate both detailed views of single records, and summary statistics for a dataset. 

#### [INSERT](https://en.wikipedia.org/wiki/Insert_(SQL))

To insert a new record into an existing table (`relation`), you can use an INSERT statement. Consider a table which has two columns, `attribute_1` and `attribute_2`. The statement:
```SQL
INSERT INTO relation (attribute_1, attribute_2) VALUES (2, 'red')
```
will insert a new record into the table `relation`, with those specified attributes. If you do not specify the attribute names above, then the values provided will match to the first two attributes of the table `relation`, by default.

To insert more than one record at once:
```SQL
INSERT INTO relation (attribute_1, attribute_2) 
	VALUES (2, 'red')
	       (3, 'blue')
```

#### [UPDATE](https://en.wikipedia.org/wiki/Update_(SQL))

If you happen to misdefine a record's attributes, you can use an UPDATE statement to fix it.
```SQL
UPDATE relation SET attribute_2 = 'green' WHERE attribute_1 = 3
```

#### [DELETE](https://en.wikipedia.org/wiki/Delete_(SQL))

To drop a single record from a table:
```SQL
DELETE FROM relation WHERE attribute_1 = 3
```

Note how, similar filters can be applied from the SELECT statements above (like WHERE) to drop more than one record. 

Furthermore, to drop all records from a table:
```SQL
DELETE FROM relation
```

To [drop](https://en.wikipedia.org/wiki/Data_definition_language#DROP_statement) an entire table:
```SQL
DROP TABLE relation
```

Now, you should understand the dilemma presented within the XKCD comic above. The school's data must be stored on a relational database, accessible via SQL. Inserting the child's name `DROP TABLE students;` has caused the entire table of student data to be lost!

### Try it Out!

There are several ways to get started learning and using SQL. The Wikipedia links that I've provided above can be helpful for understanding the basics of relational databases and SQL syntax. And below, I have provided references for online courses in SQL, as well as O'Reilly textbooks on the subject. (Some of these can be found online through the [University of Colorado Library](http://ucblibraries.summon.serialssolutions.com/search?formids=target&lang=eng&suite=def&reservedids=lang%2Csuite&submitmode=&submitname=&s.q=oreilly#!/search?ho=t&l=en&q=(%22SQL%22)%20AND%20(Publisher:(OReilly)))).

If you'd like to dive deeper, you can install your own SQL server locally. A popular relational database is [MySQL](https://www.mysql.com). If you'd rather test SQL out further before installing, Google and Wikipedia host public databases, which you can query using SQL statements. 

- [Google BigQuery](https://cloud.google.com/bigquery/public-data/): Tutorial for [querying Wikipedia data](https://codelabs.developers.google.com/codelabs/cloud-bigquery-wikipedia/index.html?index=..%2F..%2Findex#0), and [analyzing Github data](https://medium.com/google-cloud/github-on-bigquery-analyze-all-the-code-b3576fd2b150)
- [Wikipedia](https://wikitech.wikimedia.org/wiki/PAWS): [Example](https://github.com/brianckeegan/INFO-3501-5501/blob/master/Lab%201/Lab%201%20-%20Revision%20Histories.ipynb) from Brian Keegan's ["Peer Production and Crowdsourcing"](https://github.com/brianckeegan/INFO-3501-5501) course

---

### References

**Online Courses**:

- ["Learn SQL" from Codeacademy](https://www.codecademy.com/learn/learn-sql)
- ["Intro to SQL for Data Science" from DataCamp](https://www.datacamp.com/courses/intro-to-sql-for-data-science)

**Related Reading**:
- O'Reilly has several SQL-related books: ["Learning SQL: Master SQL Fundamentals"](http://a.co/3n8QFbu), ["SQL Cookbook: Query Solutions and Techniques for Database Developers"](http://a.co/fh2Ft2f), ["SQL Pocket Guide: A Guide to SQL Usage"](http://a.co/bQDAtQO)

---

Author: Allie Morgan (allison.morgan@colorado.edu) 
