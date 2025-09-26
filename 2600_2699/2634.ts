type Fn = (n: number, i: number) => any

/**
 * @see https://leetcode.cn/problems/filter-elements-from-array/description/
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
// @ts-ignore
function filter(arr: number[], fn: Fn): number[] {
  const result: number[] = []
  const l = arr.length
  for (let i = 0; i < l; i++) {
    if (fn(arr[i], i)) result.push(arr[i])
  }
  return result
};
