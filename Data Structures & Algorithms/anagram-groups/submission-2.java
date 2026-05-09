class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        Map<String, List<String>> map = new HashMap<>();

        for ( String s : strs ) {

            int[] freq = new int[26];
            for ( int i = 0; i < s.length(); i++ ) {
                freq[s.charAt(i) - 'a']++;
            }

            String key = Arrays.toString(freq);
            if ( map.containsKey(key)) {
                List<String> list = map.get(key);
                list.add(s);
                map.put(key,list);
            } else {
                List<String> list = new ArrayList<>();
                list.add(s);
                map.put(key,list);
            }
        }
        return new ArrayList<>(map.values());

    }
}
