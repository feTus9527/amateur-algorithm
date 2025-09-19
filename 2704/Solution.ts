type ToBeOrNotToBe = {
  toBe: (val: any) => boolean;
  notToBe: (val: any) => boolean;
};

/**
 * @see https://leetcode.cn/problems/to-be-or-not-to-be/description/
 * @param {string} val
 * @return {Object}
 */
// @ts-ignore
function expect(val: any): ToBeOrNotToBe {
  return {
    toBe(v) {
      if (v === val) return true
      throw "Not Equal"
    },
    notToBe(v) {
      if (v !== val) return true
      throw "Equal"
    }
  }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */
