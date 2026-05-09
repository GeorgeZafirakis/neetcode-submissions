class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {

        int rows = matrix.length;
        int cols = matrix[0].length;

        int possibleRow = 0;
        for ( int i = 0; i < rows; i++ ) {
            if ( matrix[i][cols - 1] < target ) continue;
            else if ( matrix[i][cols - 1] >= target ) {
                possibleRow = i;
                break;
            } 
        }

        for ( int i = 0; i < cols; i++ ) {
            if (matrix[possibleRow][i] == target) return true;
        }
        return false;
        
    }
}
