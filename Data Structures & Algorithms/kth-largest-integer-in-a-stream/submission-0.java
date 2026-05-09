class KthLargest {

    PriorityQueue<Integer> minHeap;
    int k;

    public KthLargest(int k, int[] nums) {
        
        this.k = k;
        this.minHeap = new PriorityQueue<>();

        for ( int num : nums ) {
            minHeap.offer(num);
            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }
    }

    public int add(int val) {

        minHeap.offer(val);
        if (minHeap.size() > k) {
            minHeap.poll();
        }
        return minHeap.peek();
    }
}


// class KthLargest {

//     List<Integer> arr;
//     int k;

//     public KthLargest(int k, int[] nums) {
//         this.k = k;
//         arr = new ArrayList();
//         for ( int i = 0; i < nums.length; i++ ) {
//             arr.add(nums[i]);
//         }
//     }
    
//     public int add(int val) {
//         arr.add(val);
//         // O(nlogn) time complexite
//         Collections.sort(arr);
//         return arr.get(arr.size() - k);
//     }
// }
