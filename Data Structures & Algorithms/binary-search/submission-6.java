public class Solution {
    
    public int binary_search(int l, int r, int[] nums, int target) {
        
        if ( l > r ) return -1;
        
        int m = ( l + r ) / 2;
        if ( nums[m] == target ) return m;
        if ( nums[m] > target )  return binary_search( l, m - 1, nums, target);
        return binary_search( m + 1, r, nums, target);
    }

    public int search(int[] nums, int target) {
        return binary_search(0, nums.length - 1, nums, target);
    }
}



// class Solution {
//     public int search(int[] nums, int target) {

//         int l = 0;
//         int r = nums.length - 1;

//         while ( l <= r ) {

//             long lm = ( l + r ) / 2;
//             int  m  = (int) lm;

//             if ( nums[m] > target) {
//                 r = m - 1;
//             } else if ( nums[m] < target) {
//                 l = m + 1;
//             } else return m;
//         }
//         return -1;
//     }
// }


// public class Solution {
//     public int search(int[] nums, int target) {
//         int index = Arrays.binarySearch(nums, target);
//         return index >= 0 ? index : -1;
//     }
// }
