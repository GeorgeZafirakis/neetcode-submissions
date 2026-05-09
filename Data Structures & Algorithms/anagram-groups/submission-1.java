class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        Map<String, List<String>> map = new HashMap<>();

        for ( String s : strs ) {

            int[] count = new int[26];
            for ( int i = 0; i < s.length(); i++ ) {
                count[s.charAt(i) - 'a']++;
            }
            String key = Arrays.toString(count);
            if ( map.containsKey(key)) {
                List<String> currList = new LinkedList<>(map.get(key));
                currList.add(s);
                map.put(key,currList);
            } else {
                List<String> valueList = new LinkedList<>();
                valueList.add(s);
                map.put(key, valueList);
            }
        }
        return new LinkedList<>(map.values());
    }
}
