import pandas as pd
import datetime
import sqlite3

cnx = sqlite3.connect('../dataframes/Northwind_large.sqlite')
c = cnx.cursor()

c.execute('SELECT * FROM employees')
results = c.fetchall()

# modality 1
employees = pd.DataFrame(results)
print(employees.head())

# modality 2
employees = pd.read_sql_query('SELECT * FROM employees', cnx)
print(employees.head())

# modality 3
employees = pd.read_sql_table('Employees', 'sqlite:///../dataframes/Northwind_large.sqlite')
print(employees.head())

tables = ['Categories', 'CustomerCustomerDemo', 'CustomerDemographics', 'Customers',
          'EmployeeTerritories', 'OrderDetails', 'orders', 'Products', 'Region',
          'Shippers', 'Suppliers', 'Territories', 'invoices',
          'purchase_order_status', 'purchase_orders', 'purchase_order_details']


# Compute the number of employees hired in each year

employees['HireDate'] = pd.to_datetime(employees['HireDate'])
employees['HireYear'] = employees['HireDate'].dt.year

output = employees.groupby('HireYear').size()
print(output)


# Find the manager (that is, employee that do not report to any other person), who have been hired the most time.

managers = employees[employees['ReportsTo'].isnull()]

output = managers.loc[managers['HireDate'].idxmin()]
print(output)


# Find the p_orders with the longest time between the submission and the approval.

p_orders = pd.read_sql_table('purchase_orders', 'sqlite:///../dataframes/Northwind_large.sqlite')
p_orders['submitted_date'] = pd.to_datetime(p_orders['submitted_date'])
p_orders['approved_date'] = pd.to_datetime(p_orders['approved_date'])

p_orders['diff'] = p_orders['approved_date'] - p_orders['submitted_date']

output = p_orders.loc[p_orders['diff'].idxmax()]
print(output)


# Find the order that has the most items

p_orders_d = pd.read_sql_table('purchase_order_details', 'sqlite:///../dataframes/Northwind_large.sqlite')

order_items = p_orders_d.groupby('purchase_order_id')['quantity'].sum()
max_items = order_items.idxmax()

output = p_orders[p_orders['id'] == max_items]
print(output)


# Compute how the current number of units in stock is distributed among all categories

products = pd.read_sql_table('Products', 'sqlite:///../dataframes/Northwind_large.sqlite')
categories_stocks = products.groupby('CategoryId')['UnitsInStock'].sum()

print(categories_stocks)


# Find the categories with the largest number of items in stock.

max_stocks = categories_stocks.idxmax()

print(max_stocks)
