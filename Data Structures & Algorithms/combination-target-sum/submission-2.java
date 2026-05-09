class Solution {

    public List<List<Integer>> combinationSum(int[] nums, int target) {
        
        Arrays.sort(nums);
        List<Integer> cur = new ArrayList<>();
        List<List<Integer>> res = new ArrayList<>();
        backtrack(nums, target, cur, 0, res);
        return res;
    }

    private void backtrack(int[] nums, int target, List<Integer> cur, int i, List<List<Integer>> res) {

        // Base Case
        if ( target == 0 ) {
            res.add(new ArrayList<>(cur));
            return;
        }

        // Base Case 2
        if (target < 0 || i >= nums.length) return;

        cur.add(nums[i]);
        backtrack(nums, target - nums[i], cur, i, res);
        cur.remove(cur.size() - 1);
        backtrack(nums, target, cur, i + 1, res);
    }
}
