import java.util.Map;
import java.util.HashMap;

/**
 * @see https://leetcode.cn/problems/two-sum/description/
 */
public class Solution {
  
  public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
      int num = nums[i];
      if (map.containsKey(target - num)) {
        return new int[] { i, map.get(target - num) };
      }
      map.put(num, i);
    }
    return new int[] { -1, -1 };
  }

  public static void main(String[] args) {
    int[] NUMS = new int[] { 3, 2, 4 };
    int TARGET = 6;

    Solution solver = new Solution();
    int[] result = solver.twoSum(NUMS, TARGET);
    System.out.println("result: " + result[0] + ", " + result[1]);
  }
} 
