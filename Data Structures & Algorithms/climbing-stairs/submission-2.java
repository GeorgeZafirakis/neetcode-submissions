class Solution {
    public int climbStairs(int n) {
        return dfs(n,0);
    }

    private int dfs(int n, int i) {

        // Base case
        if ( i >= n ) return ( i == n ) ? 1 : 0;

        // Recursive case
        return dfs(n, i + 1) + dfs(n, i + 2);

    }
}
