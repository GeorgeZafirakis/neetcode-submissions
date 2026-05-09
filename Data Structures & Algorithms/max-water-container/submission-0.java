class Solution {
    public int maxArea(int[] heights) {

        int maxArea    = 0;
        int leftIndex  = 0;
        int rightIndex = heights.length - 1;

        while ( leftIndex < rightIndex) {

            int area = ( rightIndex - leftIndex ) * Math.min( heights[leftIndex] , heights[rightIndex] );
            if ( area > maxArea) maxArea = area;

            if ( heights[leftIndex] > heights[rightIndex] ) {
                rightIndex--;
            } else {
                leftIndex++;
            }
        } 
        return maxArea;
    }
}
