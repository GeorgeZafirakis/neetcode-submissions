/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */


class Solution {
    public boolean canAttendMeetings(List<Interval> intervals) {

        Collections.sort(intervals, Comparator.comparingInt(i -> i.start));

        List<Integer> intList = new ArrayList<>();

        for (Interval interval : intervals) {
            intList.add(interval.start);  
            intList.add(interval.end);    
        }

        for (int i = 0; i < intList.size() - 1; i++) {
            if (intList.get(i + 1) < intList.get(i)) {
                return false;
            }
        }

        return true;
    }
}