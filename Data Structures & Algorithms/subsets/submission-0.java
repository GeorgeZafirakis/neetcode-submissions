class Solution {
    
    public List<List<Integer>> subsets(int[] nums) {

        List<List<Integer>> res = new ArrayList<>();
        List<Integer> subset = new ArrayList<>();
        dfs(nums, 0, subset, res);
        return res;
    }

    private void dfs(int[] nums, int i, List<Integer> subset, List<List<Integer>> res) {
        
        if ( i >= nums.length) {
            res.add(new ArrayList<>(subset));
            return;
        }

        subset.add(nums[i]);
        dfs(nums, i + 1, subset, res);
        subset.remove(subset.size() - 1);
        dfs(nums, i + 1, subset, res);


    }

}


// class Solution {
//     public List<List<Integer>> subsets(int[] nums) {

//         List<List<Integer>> res = new ArrayList<>();
//         res.add(new ArrayList<>());

//         for ( int num : nums) {
//             int size = res.size();
//             for ( int i = 0; i < size; i ++) {
//                 List<Integer> subset = new ArrayList<>(res.get(i));
//                 subset.add(num);
//                 res.add(subset);
//             }  
//         }
//         return res;
//     }
// }
