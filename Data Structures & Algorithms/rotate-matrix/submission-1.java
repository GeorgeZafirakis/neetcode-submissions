public class Solution {
    public void rotate(int[][] matrix) {
        
        int l = 0;
        int r = matrix.length - 1;

        while (l < r) {
            for (int i = 0; i < r - l; i++) {
                
                int top = l;
                int bottom = r;
                
                // Save top-left
                int temp = matrix[top][l + i];

                // Rotate in 4 steps
                matrix[top][l + i] = matrix[bottom - i][l];  // Bottom-left → Top-left
                matrix[bottom - i][l] = matrix[bottom][r - i]; // Bottom-right → Bottom-left
                matrix[bottom][r - i] = matrix[top + i][r];  // Top-right → Bottom-right
                matrix[top + i][r] = temp;  // Saved top-left → Top-right
            }
            l++;
            r--;
        }
    }
}
