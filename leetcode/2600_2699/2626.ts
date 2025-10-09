type Fn = (accum: number, curr: number) => number

/**
 * @see https://leetcode.cn/problems/array-reduce-transformation/description/
 * @param {number[]} nums
 * @param {Fn} fn
 * @param {number} init
 * @return {number}
 */
// @ts-ignore
function reduce(nums: number[], fn: Fn, init: number): number {
  let result = init
  for (let i = 0; i < nums.length; i++) {
    result = fn(result, nums[i])
  }
  return result
};
