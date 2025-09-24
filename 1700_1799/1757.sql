# @see: https://leetcode.cn/problems/recyclable-and-low-fat-products/description/

SELECT
  p.product_id AS product_id
FROM Products p WHERE p.low_fats = 'Y' and p.recyclable = 'Y';
