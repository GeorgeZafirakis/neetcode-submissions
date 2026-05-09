class Solution {
    public int leastInterval(char[] tasks, int n) {
        
        int[] count = new int[26];
        for ( char task : tasks ) {
            count[task - 'A']++;
        }

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        for ( int cnt : count) {
            if ( cnt > 0) {
                maxHeap.add(cnt);
            }
        }

        Queue<int[]> queue = new LinkedList<>();
        int time = 0;
        while ( !maxHeap.isEmpty() || !queue.isEmpty() ) {
            time++;

            if (maxHeap.isEmpty()) {
                time = queue.peek()[1];
            } else {
                int cnt = maxHeap.poll() - 1;
                if ( cnt > 0 ) {
                    queue.add(new int[] {cnt, time + n});
                }
            }

            if (!queue.isEmpty() && queue.peek()[1] == time) {
                maxHeap.add(queue.poll()[0]);
            }

        }
        return time++;
    }
}


// class Solution {
//     public int leastInterval(char[] tasks, int n) {

//         PriorityQueue<Character> minHeap = new PriorityQueue<>();
//         PriorityQueue<Character> maxHeap = new PriorityQueue<>((a,b) -> b - a);
//         int flag1 = 1;
//         int flag2 = 0;
//         int result = 0;
//         int size = tasks.length;
//         char curr;
//         char prev = '0';

//         for (char c : tasks) {
//             minHeap.offer(c);
//             maxHeap.offer(c);
//         }


//         for ( int i = 0; i < size/2; i++) {
            
//             if ( flag1 == 1) {
//                 curr = minHeap.poll();
//                 if ( curr != prev) {
//                     result++;
//                 } else {
//                     result = result + n + 1;
//                 }
//                 prev = curr;
//                 flag1 = 0;
//                 flag2 = 1;
//             }
 
//             if ( flag2 == 1) {
//                 curr = maxHeap.poll();
//                 if ( curr != prev) {
//                     result++;
//                 } else {
//                     result = result + n + 1;
//                 }
//                 prev = curr;
//                 flag2 = 0;
//                 flag1 = 1;
//             }

//         } 

//         if ( size % 2 != 0 ) {
//             curr = minHeap.poll();
//             if ( curr != prev) {
//                     result++;
//             } else {
//                     result = result + n + 1;
//             }
//         }

//         return result;
        
//     }
// }
