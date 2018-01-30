# SQL: Overview

![Comic](https://imgs.xkcd.com/comics/exploits_of_a_mom.png "Her daughter is named Help I'm trapped in a driver's license factory.")

_XKCD comic featuring SQL humor. Hopefully, by the end of this essay, you will understand the joke! ([Link](https://xkcd.com/327/))_

SQL (["Structured Query Language"](https://en.wikipedia.org/wiki/SQL)) is a language for querying, manipulating, inserting, and deleting data within _relational_ databases. The language was introduced in the [1970s](https://dl.acm.org/citation.cfm?doid=362384.362685), and has been widely in use since then. SQL can be used on large data sets, to both aggregate features of several rows, and look at single rows in detail. And even though, SQL is almost 50 years old, [many relational database systems](https://en.wikipedia.org/wiki/List_of_relational_database_management_systems) still used today, handle interactions through SQL statements.

### Database Design

[Relational databases](https://en.wikipedia.org/wiki/Relational_database) are those in which rows ("records") that contain common columns ("attributes") are stored within tables ("relations").

<img src="https://user-images.githubusercontent.com/6633242/35548378-3f09f0be-053c-11e8-9473-cad2b033350d.png" width="70%" title="Example Database">

_Example of table, featuring records, attributes, and a relation. ([Reproduction from Wikipedia](https://en.wikipedia.org/wiki/Relational_database))_

### Syntax

Using the terms from the above table, generally SQL statements follow a `SELECT/INSERT/UPDATE/DELETE ... records ... FROM/INTO/SET ... relation ... VALUES/WHERE ... attributes ...` [format](https://en.wikipedia.org/wiki/SQL_syntax). 

Let's break this apart further into four of the common SQL operations:

#### [SELECT](https://en.wikipedia.org/wiki/Select_(SQL))

#### [INSERT](https://en.wikipedia.org/wiki/Insert_(SQL))

#### [UPDATE](https://en.wikipedia.org/wiki/Update_(SQL))

#### [DELETE](https://en.wikipedia.org/wiki/Delete_(SQL))

### Try it Out!

There are several way to get started learning and using SQL. First, the Wikipedia links that I've provided above can be a helpful to understand the basics of relational databases and SQL syntax. Second, below I have provided links for online courses in SQL, as well as O'Reilly textbooks on the subject. (Some of these can be found online through the [University of Colorado Library](http://ucblibraries.summon.serialssolutions.com/search?formids=target&lang=eng&suite=def&reservedids=lang%2Csuite&submitmode=&submitname=&s.q=oreilly#!/search?ho=t&l=en&q=(%22SQL%22)%20AND%20(Publisher:(OReilly)))).

Further, you can install your own SQL server locally and get started trying to run these queries. A popular relational database is [MySQL](https://www.mysql.com) ([installation instructions](hhttps://dev.mysql.com/doc/refman/5.7/en/installing.html)).

### References

**Online Courses**:

- ["Learn SQL" from Codeacademy](https://www.codecademy.com/learn/learn-sql)
- ["Intro to SQL for Data Science" from DataCamp](https://www.datacamp.com/courses/intro-to-sql-for-data-science)

**Related Reading**:
- O'Reilly has several SQL-related books: ["Learning SQL: Master SQL Fundamentals"](http://a.co/3n8QFbu), ["SQL Cookbook: Query Solutions and Techniques for Database Developers"](http://a.co/fh2Ft2f), ["SQL Pocket Guide: A Guide to SQL Usage"](http://a.co/bQDAtQO)

---

Author: Allie Morgan (allison.morgan@colorado.edu) 
