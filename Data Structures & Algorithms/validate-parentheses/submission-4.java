class Solution {
    public boolean isValid(String s) {

        Stack<Character> stack = new Stack<>();

        if ( s.length() % 2 != 0 ) return false;

        for ( int i = 0; i < s.length(); i++) {

            if ( s.charAt(i) == '(') stack.add(')');
            else if ( s.charAt(i) == '[') stack.add(']');
            else if ( s.charAt(i) == '{') stack.add('}');
            else if ( stack.isEmpty() ) return false;
            else if ( stack.pop() != s.charAt(i)) return false;
        }
        if ( !stack.isEmpty() ) return false;
        return true;
    }
}
