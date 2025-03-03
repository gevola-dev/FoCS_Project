
--find all employees that have created at least a purchase
select distinct e.*
from Employees e, orders o
where e.Id = o.EmployeeId;

--find all employees that have created at least 2 purchases
select e.id, count(*)
from Employees e, orders o
where e.Id = o.EmployeeId
group by e.id
having count(*) >= 2;

--for each employee, compute the overall shipping fees of the purchase orders that such employee has created
select e.id, sum(i.shipping)
from Employees e, orders o, invoices i
where e.Id = o.EmployeeId
and o.id = i.order_id
group by e.id;

--for each shipper, compute the number of orders handled
select o.id, count(*)
from orders o, shippers s
where lower(o.shipName) = lower(s.CompanyName)
group by o.id;

--compute the orders shipped to the region “Western Europe”
select count(1)
from orders
where ShipRegion = "Western Europe";

--find all orders that do not have an invoice
select o.id
from orders o
left join invoices i
on o.id = i.order_id
where i.order_id is null;
