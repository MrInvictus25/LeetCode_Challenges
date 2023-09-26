/*
Table: Employees

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
+-------------+---------+
employee_id is the column with unique values for this table.
Each row of this table indicates the name of the employee whose ID is employee_id.

Table: Salaries

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| salary      | int     |
+-------------+---------+
employee_id is the column with unique values for this table.
Each row of this table indicates the salary of the employee whose ID is employee_id.
*/

SELECT emp.employee_id
FROM employees emp
LEFT JOIN salaries sal on emp.employee_id = sal.employee_id
WHERE sal.salary IS NULL
UNION

(SELECT sal.employee_id
FROM employees emp
RIGHT JOIN salaries sal on emp.employee_id = sal.employee_id
WHERE emp.name IS NULL)
ORDER BY employee_id;
