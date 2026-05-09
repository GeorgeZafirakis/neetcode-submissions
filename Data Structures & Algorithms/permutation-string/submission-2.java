class Solution {
    public boolean checkInclusion(String s1, String s2) {

        int windows = s2.length() - s1.length();
        for ( int i = 0; i <= windows; i++ ) {
            if ( sameFrequency(s1, s2.substring(i, i + s1.length()))) return true;
        }
        return false;
        
    }

    private boolean sameFrequency(String s1, String s2) {

        System.out.println("s1 = " + s1 + " s2 = " + s2);

        if ( s1.length() != s2.length() ) return false;

        int[] freq = new int[26];

        for ( int i = 0; i < s1.length(); i++) {
            freq[s1.charAt(i) - 'a']++;
            freq[s2.charAt(i) - 'a']--;
        }

        for ( int num : freq ) {
            if ( num != 0) return false;
        }
        return true;
    }
}
