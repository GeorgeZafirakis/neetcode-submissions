class Solution {
    public List<List<Integer>> subsets(int[] nums) {

        List<List<Integer>> res   = new ArrayList<>();
        List<Integer>       inner = new ArrayList<>();
        // Initialize results list [[]]
        res.add(inner);

        // Keep track of elements in nums array that have been processed
        for ( int i = 0; i < nums.length; i++ ) {
            
            // Add every new element from nums list to the inner lists of result
            int numOfInnerLists = res.size();
            for ( int k = 0; k < numOfInnerLists; k++ ) {
                // Get a copy of the sublist
                List sub = new ArrayList<>(res.get(k));
                // Add new element to the end of the list
                sub.add(nums[i]);
                // Add new list containing the nums[i] element
                res.add(sub);
            }

        }
        return res;
    }
}
