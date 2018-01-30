# SQL: Overview

![Comic](https://imgs.xkcd.com/comics/exploits_of_a_mom.png "Her daughter is named Help I'm trapped in a driver's license factory.")

_XKCD comic featuring SQL humor. Hopefully, by the end of this essay, you will understand the joke! ([Link](https://xkcd.com/327/))_

SQL (["Structured Query Language"](https://en.wikipedia.org/wiki/SQL)) is a language for querying, manipulating, inserting, and deleting data within relational databases. 
And even though, it is [almost 50 years old](https://dl.acm.org/citation.cfm?doid=362384.362685), [many relational database systems](https://en.wikipedia.org/wiki/List_of_relational_database_management_systems) still used today, handle interactions through SQL statements. In the SQL commands below, I will show how SQL can be used on large data sets, to both aggregate features of several rows, and look at single rows in detail. 

### Syntax
<!--img src="https://user-images.githubusercontent.com/6633242/35548378-3f09f0be-053c-11e8-9473-cad2b033350d.png" width="70%" title="Example Database"-->

[Relational database](https://en.wikipedia.org/wiki/Relational_database) are those in which rows ("records") that contain common columns ("attributes") are stored within tables ("relations"). Using the language of records, attributes, and relations, operations on relational databases using SQL statements generally follow a [format](https://en.wikipedia.org/wiki/SQL_syntax) that looks something like:
```{sql}
SELECT/INSERT/UPDATE/DELETE ... records ... 
	FROM/INTO/SET ... relation ... 
	VALUES/WHERE ... attributes ...
``` 

Let's take a deeper dive into four of the common SQL operations:

#### [SELECT](https://en.wikipedia.org/wiki/Select_(SQL))

#### [INSERT](https://en.wikipedia.org/wiki/Insert_(SQL))

#### [UPDATE](https://en.wikipedia.org/wiki/Update_(SQL))

#### [DELETE](https://en.wikipedia.org/wiki/Delete_(SQL))

### Try it Out!

There are several ways to get started learning and using SQL. The Wikipedia links that I've provided above can be a helpful to understand the basics of relational databases and SQL syntax. And below, I have provided references for online courses in SQL, as well as O'Reilly textbooks on the subject. (Some of these can be found online through the [University of Colorado Library](http://ucblibraries.summon.serialssolutions.com/search?formids=target&lang=eng&suite=def&reservedids=lang%2Csuite&submitmode=&submitname=&s.q=oreilly#!/search?ho=t&l=en&q=(%22SQL%22)%20AND%20(Publisher:(OReilly)))).

If you'd like to dive deeper, you can install your own SQL server locally. A popular relational database is [MySQL](https://www.mysql.com). If you'd rather test SQL out further before installing, Google and Wikipedia host public databases, which you can query using SQL statements. 

- [Google BigQuery](https://cloud.google.com/bigquery/public-data/): Tutorial for [querying Wikipedia data](https://codelabs.developers.google.com/codelabs/cloud-bigquery-wikipedia/index.html?index=..%2F..%2Findex#0), and [analyzing Github data](https://medium.com/google-cloud/github-on-bigquery-analyze-all-the-code-b3576fd2b150)
- [Wikipedia](https://wikitech.wikimedia.org/wiki/PAWS): [Example](https://github.com/brianckeegan/INFO-3501-5501/blob/master/Lab%201/Lab%201%20-%20Revision%20Histories.ipynb) from Brian Keegan

---

### References

**Online Courses**:

- ["Learn SQL" from Codeacademy](https://www.codecademy.com/learn/learn-sql)
- ["Intro to SQL for Data Science" from DataCamp](https://www.datacamp.com/courses/intro-to-sql-for-data-science)

**Related Reading**:
- O'Reilly has several SQL-related books: ["Learning SQL: Master SQL Fundamentals"](http://a.co/3n8QFbu), ["SQL Cookbook: Query Solutions and Techniques for Database Developers"](http://a.co/fh2Ft2f), ["SQL Pocket Guide: A Guide to SQL Usage"](http://a.co/bQDAtQO)

---

Author: Allie Morgan (allison.morgan@colorado.edu) 
