/**
 * @see https://leetcode.cn/problems/create-hello-world-function/descriptions/
 * @return {Function}
 */
const createHelloWorld = function (): Function {
  return function (...args: any[]): string {
    return 'Hello World'
  };
}

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */
