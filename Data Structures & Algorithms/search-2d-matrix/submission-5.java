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

        return binarySearch(matrix[possibleRow] , target);

        // for ( int i = 0; i < cols; i++ ) {
        //     if (matrix[possibleRow][i] == target) return true;
        // }
        // return false;     
    }

    private boolean binarySearch(int[] nums , int target) {

        int l = 0;
        int r = nums.length - 1;

        while ( l <= r ) {
            int m = l + ((r - l) / 2);
            if      (nums[m] > target) r = m - 1; 
            else if (nums[m] < target) l = m + 1;
            else return true;
        }
        return false;
    }
}
