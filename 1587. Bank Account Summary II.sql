# Write your MySQL query statement below
SELECT name, balance
FROM (
    SELECT Users.name, SUM(Transactions.amount) AS balance
    FROM Users
    LEFT JOIN Transactions ON Users.account = Transactions.account
    GROUP BY Users.name
    HAVING balance > 10000

    UNION

    SELECT Users.name, SUM(Transactions.amount) AS balance
    FROM Users
    RIGHT JOIN Transactions ON Users.account = Transactions.account
    GROUP BY Users.name
    HAVING balance > 10000
) AS combined
GROUP BY name, balance;