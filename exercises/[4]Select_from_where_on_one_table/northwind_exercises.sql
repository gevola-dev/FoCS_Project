
-- 1

select * 
from Products;


-- 2 

select id
from Products;

-- 3

select contactname, contacttitle 
from customers;

-- 4

select *
from employees
where ReportsTo is null;

-- 5

select count(*)
from orders;

-- 6

select customerId, count(*)
from orders
group by customerId;

-- 7

select customerId, count(*)
from orders
where shipVia = 2
group by customerId;

-- 8

select *
from customers
where country = 'Mexico'
and fax is null;
