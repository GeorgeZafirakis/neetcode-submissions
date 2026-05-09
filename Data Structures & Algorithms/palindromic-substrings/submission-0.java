class Solution {
    public int countSubstrings(String s) {
        
        int res = 0;

        for ( int i = 0; i < s.length(); i++ ) {
            res += hasPalindromes(s,i,i);
            res += hasPalindromes(s,i,i+1);
        }
        return res;
    }

    private int hasPalindromes(String s, int left, int right) {

        // if ( s.length() <= 1 ) return true;
        // int middle = s.length() / 2;
        // int left   = middle - 1;
        // int right  = middle + (s.length() % 2) ; // Odd or Even

        int res = 0;
        while ( left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right) ) {
            left--;
            right++;
            res++;
        }

        return res; 


    }
}
