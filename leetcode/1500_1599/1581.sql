# @see: https://leetcode.cn/problems/customer-who-visited-but-did-not-make-any-transactions/description/

SELECT
    c.customer_id AS customer_id,
    count(c.visit_id) AS count_no_trans
FROM Visits c LEFT JOIN Transactions t ON c.visit_id = t.visit_id
WHERE t.visit_id IS NULL
GROUP BY c.customer_id;
