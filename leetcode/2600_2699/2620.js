/**
 * @see https://leetcode.cn/problems/counter/descriptions/
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function (n) {
  let result = n
  return function () {
    return result++
  };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */
