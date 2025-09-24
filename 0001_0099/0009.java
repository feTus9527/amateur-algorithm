import java.util.Deque;
import java.util.LinkedList;

/**
 * @see https://leetcode.cn/problems/palindrome-number/description/
 */
public class Solution {

  public boolean isPalindrome(int x) {
    return isPalindrome_solution_2(x);
  }
  
  /*
   * First convert the integer to a String, then use the two-pointer method.
   *
   * Time: O(n)
   * Space: O(n)
   */
  private boolean isPalindrome_solution_1(int x) {
    if (x < 0) return false;
    String s = Integer.toString(x);
    int i = 0, j = s.length() - 1;
    while (i < j) {
      if (s.charAt(i) != s.charAt(j)) return false;
      i++;
      j--;
    }
    return true;
  }

  /* 
   * By introducing a bidirectional queue, 
   * the input integer is pushed into the queue digit by digit,
   * and then taken out from both ends for judgement.
   *
   * Time: O(n)
   * Space: O(n)
   */
  private boolean isPalindrome_solution_2(int x) {
    if (x < 0) return false;
    Deque<Integer> queue = new LinkedList<>();
    while(x > 0) {
      queue.add(x % 10);
      x /= 10;
    }
    while (queue.size() > 0) {
      if (queue.peekFirst() != queue.peekLast()) return false;
      queue.pollFirst();
      queue.pollLast();
    }
    return true;
  }
  
  /*
   * Just simply try to revert and get the last half of the integer,
   * then compare the two halves.
   *
   * Time: O(log_10(n))
   * Space: O(1)
   */
  private boolean isPalindrome_solution_3(int x) {
    if (x < 0 || (x % 10 == 0 && x != 0)) return false;
    int y = 0;
    while (y < x) {
      y = 10 * y + x % 10;
      x /= 10;
    }
    return x == y || x == y / 10;
  }

  public static void main(String[] args) {
    int X = 121;
    Solution solver = new Solution();
    boolean result = solver.isPalindrome(X);
    System.out.println("result: " + result);
  }
}
