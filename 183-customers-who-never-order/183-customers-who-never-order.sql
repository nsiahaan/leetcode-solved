# Write your MySQL query statement below
    SELECT Customers.name as Customers
    FROM Customers
    LEFT JOIN Orders ON Orders.customerID = Customers.id
    WHERE Orders.customerId IS NULL;