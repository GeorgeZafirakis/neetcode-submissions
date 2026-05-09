class Solution {
    public int findKthLargest(int[] nums, int k) {

        PriorityQueue<Integer> minHeap = new PriorityQueue<>((a , b) -> b - a);

        for ( int num : nums) {
            minHeap.offer(num);
        }

        for (int i = 0; i < k - 1; i++) {
            minHeap.poll();
        }
        return minHeap.peek();
    }
}


// class Solution {
//     public int findKthLargest(int[] nums, int k) {

//         Arrays.sort(nums);
//         return nums[nums.length - k];
        
//     }
// }
