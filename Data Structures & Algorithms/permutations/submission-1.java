class Solution {
    public List<List<Integer>> permute(int[] nums) {
        
        List<List<Integer>> perms = new ArrayList<>();
        perms.add(new ArrayList<>());

        for ( int num : nums ) {
            List<List<Integer>> new_perms = new ArrayList<>();
            for ( List<Integer> p : perms ) { // [1]
                for ( int i = 0; i <= p.size(); i++ ) {
                    List<Integer> p_copy = new ArrayList<>(p);
                    // Using add(index,num) we can add the new number in all possible positions
                    p_copy.add(i,num); // [2,1] [1,2] 
                    new_perms.add(p_copy); // [[2,1],[1,2]]
                }
            }
            perms = new_perms; // [[2,1],[1,2]]
        }
        return perms;
    }
}
