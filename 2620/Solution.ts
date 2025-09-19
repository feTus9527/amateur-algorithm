/**
 * @see https://leetcode.cn/problems/counter/descriptions/
 * @param {number} n
 * @return {Function} counter
 */
// @ts-ignore
function createCounter(n: number): () => number {
  let result: number = n
  return function (): number {
    return result++
  };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */
