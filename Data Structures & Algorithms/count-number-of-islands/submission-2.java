class Solution {

    private final int[][] directions = {{1,0} , {-1,0},
                                        {0,1} , {0,-1}};

    public int numIslands(char[][] grid) {

        int islands = 0;
        for ( int r = 0; r < grid.length; r++ ) {
            for ( int c = 0; c < grid[0].length; c++ ) {
                if (grid[r][c] == '1') {
                    islands++;
                    // bfs(grid, r, c);
                    dfs(grid, r, c);
                }
            }
        }
        return islands; 
    }

    private void dfs(char[][] grid, int r, int c) {

        // Base case
        if ( r < 0 || c < 0 || r >= grid.length || c >= grid[0].length || grid[r][c] == '0') return;

        // Access grid globally and set current position with value 1 to 0
        grid[r][c] = '0';

        for ( int[] dir : directions ) {
            dfs(grid, r + dir[0], c + dir[1]);
        }
    }

    private void bfs(char[][] grid, int r, int c) {
        
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] {r,c});
        grid[r][c] = '0';

        while (!queue.isEmpty()) {
            int[] node = queue.poll();
            int row = node[0];
            int col = node[1];

            for ( int[] dir : directions ) {
                int nr = row + dir[0];
                int nc = col + dir[1];

                if (nr >= 0 && nc >=0 && nr < grid.length && nc < grid[0].length && grid[nr][nc] == '1' ) {
                    grid[nr][nc] = '0';
                    queue.add(new int[] {nr,nc});
                }
            }
        }
    }

}
