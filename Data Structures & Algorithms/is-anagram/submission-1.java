class Solution {
    public boolean isAnagram(String s, String t) {

        if ( s.length() != t.length() ) return false;

        char[] w1 = s.toCharArray();
        char[] w2 = t.toCharArray();

        int[] freq1 = new int[26];
        int[] freq2 = new int[26];

        for ( char c : w1) {
            freq1[c - 'a']++;
        }

        for ( char c : w2) {
            freq2[c - 'a']++;
        }

        for ( int i = 0; i < 26; i++ ) {
            if ( freq1[i] != freq2[i] ) return false;
        }

        return true;

    }
}
