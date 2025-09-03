/**
 *
 * @see https://leetcode.cn/problems/two-sum/description/
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  const store = {};
  for (let i = 0; i < nums.length; i++) {
    if (store[target - nums[i]] !== void 0) return [i, store[target - nums[i]]]
    store[nums[i]] = i
  }
  return [-1, -1]
};
