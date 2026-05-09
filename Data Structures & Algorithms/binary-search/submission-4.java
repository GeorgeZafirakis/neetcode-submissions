class Solution {
    public int search(int[] nums, int target) {

        int l = 0;
        int r = nums.length - 1;

        while ( l <= r ) {

            long lm = ( l + r ) / 2;
            int m   = (int) lm;

            if ( nums[m] > target) {
                r = m - 1;
            } else if ( nums[m] < target) {
                l = m + 1;
            } else return m;
        }
        return -1;
    }
}


// public class Solution {
//     public int search(int[] nums, int target) {
//         int index = Arrays.binarySearch(nums, target);
//         return index >= 0 ? index : -1;
//     }
// }
