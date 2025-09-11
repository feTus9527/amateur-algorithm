/**
 * @see https://leetcode.cn/problems/create-hello-world-function/descriptions/
 * @return {Function}
 */
const createHelloWorld = function () {
  return (..._) => 'Hello World'
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */
