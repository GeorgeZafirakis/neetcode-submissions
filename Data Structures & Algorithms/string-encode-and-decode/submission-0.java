class Solution {

    public String encode(List<String> strs) {
        StringBuilder res = new StringBuilder();
        for ( String s : strs ) {
            res.append(s.length()).append('@').append(s);
        }
        return res.toString();
    }


    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int i = 0;

        while (i < str.length()) {
            // Find the position of '@'
            int j = i;
            while (j < str.length() && str.charAt(j) != '@') {
                j++;
            }

            // Extract the length of the next word
            int length = Integer.parseInt(str.substring(i, j));
            i = j + 1; // Move past '@'

            // Extract the word
            String word = str.substring(i, i + length);
            res.add(word);

            // Move `i` to the start of the next encoded word
            i += length;
        }
        return res;
    }
}


