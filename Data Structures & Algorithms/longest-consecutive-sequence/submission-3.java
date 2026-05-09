class Solution {
    public int longestConsecutive(int[] nums) {

        if (nums.length == 0) return 0;

        // O(nlogn) time complexity due to sorting
        Arrays.sort(nums);

        int maxSeq = 1; // The longest sequence found
        int seq = 1; // Current sequence length

        for (int i = 1; i < nums.length; i++) {

            // Skip duplicates
            if (nums[i] == nums[i - 1]) {
                continue;
            }

            // If the current number is consecutive to the previous one
            if (nums[i] == nums[i - 1] + 1) {
                seq++;
            } else {
                // Reset the sequence length if it's not consecutive
                maxSeq = Math.max(maxSeq, seq);
                seq = 1; // Start a new sequence
            }
        }

        // Final check for the last sequence
        return Math.max(maxSeq, seq);
    }
}
