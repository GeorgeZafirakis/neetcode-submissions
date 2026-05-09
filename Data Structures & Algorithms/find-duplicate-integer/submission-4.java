class Solution {
    public int findDuplicate(int[] nums) {

        int dupl = -1;

        for ( int num : nums ) {
            int idx = Math.abs(num) -1;
            if (nums[idx] < 0) dupl = Math.abs(num);
            nums[idx] *= -1;
        }

        // Make sure I do not mess the original nums array
        for ( int i = 0; i < nums.length; i++ ) {
            if ( nums[i] < 0 ) nums[i] = (-1)*nums[i];
        }

        System.out.println(Arrays.toString(nums));
        
        return dupl;
    }
}
