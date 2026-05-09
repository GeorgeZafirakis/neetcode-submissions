public class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Count the frequency of each number [(num , freq) ... (numX, freqX)]
        Map<Integer, Integer> countMap = new HashMap<>();
        for ( int num : nums ) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }

        // Create an array of lists
        List<Integer>[] frequencyBuckets = new List[nums.length + 1];
        for ( int i = 0; i < frequencyBuckets.length; i++ ) {
            frequencyBuckets[i] = new ArrayList<>();
        }

        // Place numbers into corresponding frequency buckets
        for ( Map.Entry<Integer,Integer> entry : countMap.entrySet() ) {
            int number = entry.getKey();
            int freq   = entry.getValue();
            frequencyBuckets[freq].add(number);
        }

        // for ( int i = 0; i < frequencyBuckets.length; i++ ) {
        //     System.out.println("i: " + i + " values: " + frequencyBuckets[i].toString() );
        // }

        // Collect the top K frequent elements
        int result[] = new int[k];
        int index = 0;

        for ( int i = frequencyBuckets.length - 1; i >= 0; i-- ) {
            for ( int num : frequencyBuckets[i] ) {
                result[index++] = num;
                if ( index == k ) {
                    return result;
                }
            }
        }
        return result;
    }
}