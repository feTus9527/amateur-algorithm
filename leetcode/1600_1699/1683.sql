# @see: https://leetcode.cn/problems/invalid-tweets/description/

SELECT
  t.tweet_id AS tweet_id
FROM Tweets t
WHERE CHAR_LENGTH(t.content) > 15;
