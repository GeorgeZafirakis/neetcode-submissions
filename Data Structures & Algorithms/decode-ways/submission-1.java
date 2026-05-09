class Solution {
    
    public int numDecodings(String s) {

        int[] dp = new int[s.length() + 1];
        dp[s.length()] = 1;

        for ( int i = s.length() - 1; i >= 0; i-- ) {

            if (s.charAt(i) == '0') dp[i] = 0;
            else {
                dp[i] = dp[i+1];
                if ((i+1 < s.length()) && 
                ((s.charAt(i) == '1') || (s.charAt(i) == '2' && s.charAt(i+1) < '7'))) {
                    dp[i] += dp[i+2];
                }
            }
        }
        return dp[0];
    }
}

// class Solution {
    
//     public int numDecodings(String s) {
//         return dfs(0,s);
//     }

//     private int dfs(int i, String s) {

//         if ( i == s.length() )   return 1;
//         if ( s.charAt(i) == '0') return 0;

//         int res = dfs(i+1, s);
//         if (i < s.length() - 1) {
//             if (s.charAt(i) == '1' ||
//                 s.charAt(i) == '2' && s.charAt(i+1) < '7') {
//                     res += dfs(i+2, s);
//                 }
//         }
//         return res;
//     }
// }
