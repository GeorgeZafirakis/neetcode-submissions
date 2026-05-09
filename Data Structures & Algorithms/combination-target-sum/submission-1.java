public class Solution {

    List<List<Integer>> res;
    
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        res = new ArrayList<List<Integer>>();
        List<Integer> cur = new ArrayList();
        backtrack(nums, target, cur, 0);
        return res;
    }

    public void backtrack(int[] nums, int target, List<Integer> cur, int index) {
        if (target == 0) {
            res.add(new ArrayList(cur));
            return;
        }
        if (target < 0 || index >= nums.length) {
            return;
        }

        cur.add(nums[index]);
        backtrack(nums, target - nums[index], cur, index);
        cur.remove(cur.size() - 1);
        backtrack(nums, target, cur, index + 1);
    }
}