
--Find the employees that have created no purchases (using a set operation)
 SELECT id
 FROM Employees
 EXCEPT
 SELECT EmployeeId
 FROM orders;
 
--Find the employees that have created no purchases (not using a set operation)
select e.id
from Employees e
left join Orders o
on e.id = o.EmployeeId
where o.EmployeeId is null;

--Find the orders placed by a custormer in Austria or in Venezuela (using a set operation)
select id
from Orders
where CustomerId in ( 
	select CustomerId
	from Orders
	INTERSECT
	select Id
	from Customers
	where country in ("Austria","Venezuela"));
	
--Find the orders placed by a custormer in Austria or in Venezuela (not using a set operation)
select o.id
from Orders o, Customers c 
where o.CustomerId = c.id
and c.country in ("Austria","Venezuela");

--Compute the total number of items (quantity) to be shipped to Italy.
select sum(d.quantity)
from Orders o, orderdetails d
where o.id = d.orderid
and o.ShipCountry = "Italy";

--Compute the cities that have a customer and are the destination of a shipment.
select count(*)
from (
	select distinct ShipCity
	from Orders
	where ShipCity is not null
	intersect
	select distinct ShipCity
	from Orders
	where CustomerId is not null);

--Compute the cities that have a customer or are the destination of a shipment.
select count(*)
from (
	select distinct ShipCity
	from Orders
	where ShipCity is not null
	union
	select distinct ShipCity
	from Orders
	where CustomerId is not null);

--Compute the cities that are the destination of a shipment but have no customer.
select count(*)
from (
	select distinct ShipCity
	from Orders
	where ShipCity is not null
	intersect
	select distinct ShipCity
	from Orders
	where CustomerId is null);

