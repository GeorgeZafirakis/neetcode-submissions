class Solution {
    public int lastStoneWeight(int[] stones) {

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>( (a , b) -> b - a );

        // Have all rocks sorted with the largest on top
        for ( int stone : stones ) {
            maxHeap.offer(stone);
        }

        while ( maxHeap.size() >= 2 ) {
            int larger   = maxHeap.poll();
            int smaller  = maxHeap.poll();
            int result   = larger - smaller;

            if ( result > 0 ) {
                maxHeap.offer(result);
            }

            // If no rocks have remained, return 0
            if ( maxHeap.size() == 0) {
                return 0;
            }
        }

        // If a single rock has remained, return this rock
        return maxHeap.poll();
        
    }
}
