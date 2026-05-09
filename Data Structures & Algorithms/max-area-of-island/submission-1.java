class Solution {

    private final int[][] dirs = {{-1,0},{1,0},{0,-1},{0,1}};

    public int maxAreaOfIsland(int[][] grid) {

        int ROWS = grid.length;
        int COLS = grid[0].length;
        int islands = 0;

        for ( int r = 0; r < ROWS; r++ ) {
            for ( int c = 0; c < COLS; c++) {
                if ( grid[r][c] == 1) {
                    int res = dfs(grid, r, c);
                    islands = Math.max(res, islands);
                }
            }
        }
        return islands;
    }

    private int dfs(int[][] grid, int r, int c) {

        // Base Case
        if ( r < 0 || c < 0 || r >= grid.length || c >= grid[0].length || grid[r][c] == 0) {
            return 0;
        }

        // Recursive Case
        grid[r][c] = 0;
        int res = 1;
        for ( int[] dir : dirs) {
            int nr = r + dir[0];
            int nc = c + dir[1];
            res += dfs(grid, nr, nc);
        }
        return res;
    }
}
