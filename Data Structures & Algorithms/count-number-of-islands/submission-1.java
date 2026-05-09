class Solution {

    private final int[][] directions = {{1,0} , {-1,0},
                                        {0,1} , {0,-1}};

    public int numIslands(char[][] grid) {

        int islands = 0;
        for ( int r = 0; r < grid.length; r++ ) {
            for ( int c = 0; c < grid[0].length; c++ ) {
                if (grid[r][c] == '1') {
                    islands++;
                    bfs(grid, r, c);
                }
            }
        }
        return islands; 
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
