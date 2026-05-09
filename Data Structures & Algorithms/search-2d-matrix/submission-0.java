class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {

        int height  = matrix.length;
        int width   = matrix[0].length;
        int w = 0;
        int h = height - 1;

        while ( h >= 0 && w < width ) {
            
            if (matrix[h][w] > target) {
                h--;
            } else if ( matrix[h][w] < target ) {
                w++;
            } else {
                return true;
            }
        }
        return false;
    }
}
