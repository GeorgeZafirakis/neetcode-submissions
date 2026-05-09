public class Solution {
    public boolean isValidSudoku(char[][] board) {

        Map<Integer, Set<Character>> cols    = new HashMap<>();
        Map<Integer, Set<Character>> rows    = new HashMap<>();
        Map<String,  Set<Character>> squares = new HashMap<>();

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') continue;

                String squareKey = (r / 3) + "," + (c / 3);

                // Get the set or create a new one
                rows.putIfAbsent(r, new HashSet<>());
                cols.putIfAbsent(c, new HashSet<>());
                squares.putIfAbsent(squareKey, new HashSet<>());

                // Check for duplicates
                if (rows.get(r).contains(board[r][c]) ||
                    cols.get(c).contains(board[r][c]) ||
                    squares.get(squareKey).contains(board[r][c])) {
                    return false;
                }

                // Add the value to the sets
                rows.get(r).add(board[r][c]);
                cols.get(c).add(board[r][c]);
                squares.get(squareKey).add(board[r][c]);
            }
        }
        return true;
    }
}



// public class Solution {
//     public boolean isValidSudoku(char[][] board) {

//         // Check we have no duplicates in columns
//         for ( int row = 0; row < 9; row++) {
//             Set<Character> set = new HashSet<>();
//             for ( int i = 0; i < 9; i++) {
//                 if (board[row][i] == '.') continue;
//                 if (set.contains(board[row][i])) return false;
//                 set.add(board[row][i]);
//             }
//         }

//         // Check we have no duplicates in rows
//         for ( int col = 0; col < 9; col++) {
//             Set<Character> set = new HashSet<>();
//             for ( int i = 0; i < 9; i++) {
//                 if (board[i][col] == '.') continue;
//                 if (set.contains(board[i][col])) return false;
//                 set.add(board[i][col]);
//             }
//         }

//         // Check no duplicates in squares
//         for ( int square = 0; square < 9; square++) {
//             Set<Character> set = new HashSet<>();
//             for (int i = 0; i < 3; i++) {
//                 for (int j = 0; j < 3; j++) {
//                     int row = (square / 3) * 3 + i;
//                     int col = (square % 3) * 3 + j;
//                     if (board[row][col] == '.') continue;
//                     if (set.contains(board[row][col])) return false;
//                     set.add(board[row][col]);
//                 }
//             }
//         }

//         return true;

//     }
// }