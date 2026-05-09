class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        
        int n = nums.length;
        int[] output = new int[n - k + 1]; // Array to store max values
        Deque<Integer> q = new LinkedList<>(); // Store indices of nums[]
        int l = 0, r = 0; // Left and right pointers for the window

        while (r < n) {

            // 1️⃣ Remove all elements smaller than nums[r] from the back of deque
            while (!q.isEmpty() && nums[q.getLast()] < nums[r]) {
                q.removeLast();
            }

            // 2️⃣ Add current index at the back
            q.addLast(r);

            // 3️⃣ Remove the leftmost element if it's outside the window
            if (l > q.getFirst()) {
                q.removeFirst();
            }

            // 4️⃣ Store the max value for the current window
            if ((r + 1) >= k) {  // Start recording max once we have a valid window
                output[l] = nums[q.getFirst()]; // Max is at the front
                l++; // Move the window forward
            }

            r++; // Expand the window
        }

        return output;
    }
}
