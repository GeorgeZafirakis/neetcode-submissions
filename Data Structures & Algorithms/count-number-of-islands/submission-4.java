class Solution {

    private final int[][] dirs = {{-1,0},{1,0},{0,-1},{0,1}};

    public int numIslands(char[][] grid) {

        int ROWS = grid.length;
        int COLS = grid[0].length;
        int islands = 0;

        for ( int r = 0; r < ROWS; r++ ) {
            for ( int c = 0; c < COLS; c++ ) {
                if ( grid[r][c] == '1' ) {
                    // dfs(grid,r,c);
                    bfs(grid,r,c);
                    islands++;
                }
            }
        }
        return islands;
    }

    private void dfs(char[][] grid, int r, int c) {

        // Base Case
        if ( r < 0 || c < 0 || r >= grid.length || c >= grid[0].length || grid[r][c] == '0') return;

        // Recursive case
        grid[r][c] = '0';
        for (int[] dir : dirs) {
            dfs(grid, r + dir[0], c + dir[1]);
        }
    }  

    private void bfs(char[][] grid, int r, int c) {

        Queue<int[]> q = new LinkedList<>();
        grid[r][c] = '0';
        q.add(new int[] {r,c});

        while (!q.isEmpty()) {
            int[] node = q.poll();
            int row = node[0];
            int col = node[1];

            for (int[] dir : dirs) {
                int nr = row + dir[0];
                int nc = col + dir[1];
                if (nr >= 0 && nc >= 0 && nr < grid.length && nc < grid[0].length && grid[nr][nc] == '1') {
                    q.add(new int[] {nr,nc});
                    grid[nr][nc] = '0';
                }
            }
        }
    }  












}

