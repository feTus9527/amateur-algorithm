type Counter = {
  increment: () => number,
  decrement: () => number,
  reset: () => number,
}

/**
 * @see https://leetcode.cn/problems/counter-ii/description/
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
// @ts-ignore
var createCounter = function (init: number): Counter {
  let counter = init
  return {
    increment() {
      return ++counter
    },
    decrement() {
      return --counter
    },
    reset() {
      counter = init
      return counter
    }
  }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
