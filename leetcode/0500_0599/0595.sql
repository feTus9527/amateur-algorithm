# @see https://leetcode.cn/problems/big-countries/description/

SELECT
  w.name AS name,
  w.population AS population,
  w.area AS area
FROM World w WHERE w.area >= 3000000 OR w.population >= 25000000;
