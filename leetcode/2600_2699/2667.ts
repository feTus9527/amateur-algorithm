/**
 * @see https://leetcode.cn/problems/create-hello-world-function/descriptions/
 * @return {Function}
 */
// @ts-ignore
const createHelloWorld = function (): Function {
  return function (..._: any[]): string {
    return 'Hello World'
  };
}

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */
