# @see: https://leetcode.cn/problems/replace-employee-id-with-the-unique-identifier/description/

SELECT
    uni.unique_id AS unique_id,
    e.name AS name
FROM Employees e LEFT JOIN EmployeeUNI uni ON e.id = uni.id;
