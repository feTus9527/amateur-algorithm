/**
 * @see https://leetcode.cn/problems/apply-transform-over-each-element-in-array/description/
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
// @ts-ignore
var map = function (arr: number[], fn: (n: number, i: number) => number): number[] {
  const l = arr.length
  for (let i = 0; i < l; i++) {
    arr[i] = fn(arr[i], i)
  }
  return arr
};
