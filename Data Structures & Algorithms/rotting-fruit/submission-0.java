class Solution {
    public int orangesRotting(int[][] grid) {
        int ROWS = grid.length;
        int COLS = grid[0].length;
        Queue<int[]> q = new LinkedList<>();
        int freshOranges = 0; // Track fresh oranges

        // Add all rotten oranges to queue and count fresh ones
        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                if (grid[i][j] == 2) {
                    q.add(new int[]{i, j});
                } else if (grid[i][j] == 1) {
                    freshOranges++;
                }
            }
        }

        // If there are no fresh oranges, return 0
        if (freshOranges == 0) return 0;

        int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int time = 0;

        // BFS traversal
        while (!q.isEmpty()) {
            int size = q.size();
            boolean rotted = false; // Check if at least one orange gets rotten this round
            
            for (int i = 0; i < size; i++) {
                int[] cell = q.poll();
                int r = cell[0];
                int c = cell[1];

                for (int[] dir : dirs) {
                    int nr = r + dir[0];
                    int nc = c + dir[1];

                    if (nr >= 0 && nc >= 0 && nr < ROWS && nc < COLS && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2; // Mark orange as rotten
                        q.add(new int[]{nr, nc});
                        freshOranges--; // Reduce count of fresh oranges
                        rotted = true;
                    }
                }
            }

            if (rotted) time++; // Increase time only if at least one orange was rotted this round
        }

        return freshOranges == 0 ? time : -1; // If any fresh oranges remain, return -1
    }
}

