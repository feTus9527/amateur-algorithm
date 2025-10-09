/**
 * @see https://leetcode.cn/problems/filter-elements-from-array/description/
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function (arr, fn) {
  const result = []
  const l = arr.length
  for (let i = 0; i < l; i++) {
    if (fn(arr[i], i)) result.push(arr[i])
  }
  return result
};
