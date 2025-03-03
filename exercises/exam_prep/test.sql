
-- Exercise 1 

--Basic Selection: Write a query to retrieve all authors with an income greater than 65,000.
select *
from authors
where income > 65000;

--Ordering: Write a query to get all authors, ordered by their last name alphabetically.
select *
from authors
order by last_name asc;

-- Exercise 2: Working with Multiple Tables (Joins)
-- Using the Authors, Books, and BooksAuthors tables:

-- Inner Join: Write a query to find the first and last names of authors who have written a book with ID 1.
select a.first_name, a.last_name
from authors a, books b, booksAuthors c
where a.id = c.id_author
and b.id = c.id_book
and b.id = 1;

-- Left Join: List all authors and include the titles of books they have written, if any.
select a.id_author, b.title
from booksAuthors c
join authors a on a.id = c.id_author 
left join books b on b.id = c.id_book;


--Exercise 3: Set Operations

--Union: Write a query to find authors with an income over 90,000 or authors whose last name contains the letter 'o'​(04-set-operations).
select id
from authors
where income > 90000
Union
select id
from authors
where last_name like '%o%';

--Intersect: Retrieve authors who earn more than 90,000 and whose last name contains the letter 'o'​(05-nested-queries).
select id
from authors
where income > 90000
Intersect
select id
from authors
where last_name like '%o%';

--Except: Write a query to find authors with income over 90,000 except those whose last name contains the letter 'o'​(04-set-operations).
select id
from authors a
where income > 90000
except
select 1
from authors b
where b.last_name like '%o%';

--Exercise 4: Nested Queries

--Subquery with ANY: Find authors who have the highest income.
select *
from authors
where income = (select max(income) from authors);

--Subquery with IN: Write a query to find the names of all authors who have written books with ISBNs ending in the digit '5'​(03-sql-more-tables (1)).
select a.first_name, a.last_name
from authors a
join booksAuthors c on c.id_author = a.id
where c.id_book in (select b.id from books b where ISBNs like '%5');

--NOT IN Subquery: Write a query to list authors who have not written any book.
select a.*
from authors a
where a.id not in (select b.id_author from booksAuthors b);


--------------------------------------------------------------------------------------------------

--Exercise 1: Aggregations and Conditional Logic
--Using the Authors and BooksAuthors tables:

--Income Bands: Write a query that classifies authors into income bands (e.g., Low: <50,000, Medium: 50,000-100,000, High: >100,000) and returns the count of authors in each band.
select case
    when income < 500000 then 'Low'
    when income > 500000 and income < 1000000 then 'Medium'
    when income > 1000000 then 'High'
end as band,
count(1)    
from authors
group by band;

--Conditional Aggregate with CASE: For each genre, calculate the average income, but only include authors with an income greater than 60,000.
--Use CASE inside an aggregate function to filter income conditions.
select
    genre,
    case 
        when income > 60000 then avg(income)
        else null
    end
from authors
group by genre;

--Income Percentile Calculation: Write a query to calculate the percentile rank of each author's income within their genre. 
--The percentile rank should be calculated as rank / total_authors_in_genre.
select genre, (select count(1) from authors) / count(1)
from authors
group by genre;
