class Solution {

    private final int[][] directions = {{1,0} , {-1,0},
            {0,1} , {0,-1}};

    public int maxAreaOfIsland(int[][] grid) {

        int area = 0;
        int maxArea = 0;

        for ( int r = 0; r < grid.length; r++ ) {
            for ( int c = 0; c < grid[0].length; c++ ) {
                if (grid[r][c] == 1) {
                    int before = count1sInGrid(grid);
                    dfs(grid, r, c);
                    int after = count1sInGrid(grid);
                    area = before - after;
                    if ( area > maxArea ) maxArea = area;
                }
            }
        }
        return maxArea;
    }

    private int count1sInGrid(int[][] grid) {

        int area = 0;

        for ( int r = 0; r < grid.length; r++ ) {
            for (int c = 0; c < grid[0].length; c++) {
                if (grid[r][c] == 1) area++;
            }
        }
        return area;
    }

    private void dfs(int[][] grid, int r, int c) {

        // Base case
        if ( r < 0 || c < 0 || r >= grid.length || c >= grid[0].length || grid[r][c] == 0) return;

        // Access grid globally and set current position with value 1 to 0
        grid[r][c] = 0;

        for ( int[] dir : directions ) {
            dfs(grid, r + dir[0], c + dir[1]);
        }
    }

}