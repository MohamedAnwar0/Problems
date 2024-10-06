# Write your MySQL query statement below
SELECT EmployeeUNI.unique_id , Employees.name
FROM Employees
LEFT JOIN EmployeeUNI USING(id);

# time = 1104 ms # beats 59.78% 
#######################################

# Write your MySQL query statement below
SELECT EmployeeUNI.unique_id , Employees.name
FROM Employees
LEFT JOIN EmployeeUNI 
ON Employees.id = EmployeeUNI.id;

# time = 948 ms # beats 93.53%
