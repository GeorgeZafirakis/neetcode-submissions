class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0) return 0; 

        int l = 0;
        int maxLength = 0;

        Set<Character> buf = new HashSet<>();

        for (int r = 0; r < s.length(); r++) {
            if (!buf.contains(s.charAt(r))) {
                buf.add(s.charAt(r));
            } else {
                while (buf.contains(s.charAt(r))) {
                    buf.remove((Character) s.charAt(l)); 
                    l++;
                }
                buf.add(s.charAt(r));
            }
            maxLength = Math.max(maxLength, buf.size());
        }
        return maxLength;
    }
}