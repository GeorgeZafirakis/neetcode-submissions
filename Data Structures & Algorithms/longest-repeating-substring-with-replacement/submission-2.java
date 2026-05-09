class Solution {
    public int characterReplacement(String s, int k) {
        if (s.length() == 0) return 0;

        int l = 0, maxFreq = 0, maxSeq = 0;
        int[] freq = new int[26];

        for (int r = 0; r < s.length(); r++) {
            freq[s.charAt(r) - 'A']++;
            maxFreq = Math.max(maxFreq, freq[s.charAt(r) - 'A']);

            // If the remaining characters in the window are more than k, shrink from left
            while ((r - l + 1) - maxFreq > k) {
                freq[s.charAt(l) - 'A']--;
                l++;
            }

            maxSeq = Math.max(maxSeq, r - l + 1);
        }

        return maxSeq;
    }
}