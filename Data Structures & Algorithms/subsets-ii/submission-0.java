// class Solution {
//     public List<List<Integer>> subsetsWithDup(int[] nums) {
        
//     }
// }

public class Solution {
    
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Set<List<Integer>> res = new HashSet<>();
        List<Integer> subset   = new ArrayList<>();
        Arrays.sort(nums);
        dfs(nums, 0, subset, res);
        return new ArrayList<>(res);
    }

    private void dfs(int[] nums, int i, List<Integer> subset, Set<List<Integer>> res) {
        
        // Base Case
        if ( i >= nums.length ) {
            res.add(new ArrayList<>(subset));
            return;
        }

        // Recursive case
        subset.add(nums[i]);
        dfs(nums, i+1, subset, res);
        subset.remove(subset.size() - 1);
        dfs(nums, i+1, subset, res);
    }
}
