# @see: https://leetcode.cn/problems/find-customer-referee/description/

SELECT
  c.name AS name
FROM Customer c WHERE c.referee_id != 2 OR c.referee_id IS NULL;
