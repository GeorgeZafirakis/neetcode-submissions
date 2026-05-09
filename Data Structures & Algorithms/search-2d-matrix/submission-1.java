public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int ROWS = matrix.length;
        int COLS = matrix[0].length;

        int top = 0;
        int bot = ROWS - 1;

        while ( top <= bot ) {
            int row = ( top + bot ) / 2;
            if ( target > matrix[row][COLS - 1]) {
                top = row + 1;
            } else if ( target < matrix[row][0]) {
                bot = row - 1;
            } else {
            break;
            }
        }

        if (!( top <= bot)) {
            return false;
        }

        int row = ( top + bot ) / 2;
        int l = 0;
        int r = COLS - 1;
        while (l <= r) {
            int m = (l + r) / 2;
            if (target > matrix[row][m]) {
                l = m + 1;
            } else if (target < matrix[row][m]) {
                r = m - 1;
            } else {
                return true;
            }
        }
        return false;
    }
}


// class Solution {
//     public boolean searchMatrix(int[][] matrix, int target) {

//         int height  = matrix.length;
//         int width   = matrix[0].length;
//         int w = 0;
//         int h = height - 1;

//         while ( h >= 0 && w < width ) {
            
//             if (matrix[h][w] > target) {
//                 h--;
//             } else if ( matrix[h][w] < target ) {
//                 w++;
//             } else {
//                 return true;
//             }
//         }
//         return false;
//     }
// }
