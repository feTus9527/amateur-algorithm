# @see: https://leetcode.cn/problems/article-views-i/description/

SELECT distinct 
  v.author_id AS id
FROM Views v WHERE v.author_id = v.viewer_id
ORDER BY id;
