
--Find the product with highest unitprice
select id, ProductName, UnitPrice
from products
where UnitPrice in (
	select max(UnitPrice)
	from Products
);

--Find the employees that have managed at least an order, but have created no purchase order
select distinct E.id, E.LastName, E.FirstName
from employees E join orders on E.id=orders.employeeid
where not exists (select *
                  from purchase_orders
                  where E.id = purchase_orders.created_by);

--Find the countries that have at least a customer, but no supplier
select distinct Country
from Customers
where country not in (select country from suppliers);

