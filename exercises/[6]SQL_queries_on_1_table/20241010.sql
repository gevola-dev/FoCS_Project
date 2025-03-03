
--The customers whose country is Italy, France or Austria
select *
from Customers
where country in ('Italy','France','Austria');

--The customers whose address contains the word 'rue'.
select *
from Customers
where address like '%rue%';

--The customers whose City is at least 5 characters long.
select *
from Customers
where length(City) >= 5;

--The products with ID larger than 20.
select *
from Products
where id > 20;

--The (unique) customers IDs that have placed at least an order.
select distinct(customerid)
from Orders; 

--The customers IDs that have placed at least 150 orders.
select customerid, count(1) as ordini
from Orders
group by customerid
having count(1) >= 150;

--For each order, the total amount of products (quantities) sold.
select orderid, sum(quantity) as quantità
from orderdetails
group by orderid;

--For each order, the total amount of products (quantities) sold and the average discount offered if non-zero. The result must be one table.
select orderid, sum(quantity) as quantità, avg(Discount) as "sconto medio"
from orderdetails
group by orderid;

--For each order, the total price (in units).
select orderid, sum(UnitPrice) as "costo totale"
from orderdetails
group by orderid;

--For each product, the total amount of units sold.
select productid, sum(quantity) as "totale venduto"
from orderdetails
group by productid;

--For each product, the average units sold per order.
select productid, sum(quantity)/count(orderid) as "media quantità x ordine"
from orderdetails
group by productid;
