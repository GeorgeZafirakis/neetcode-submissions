class Solution {
    public int evalRPN(String[] tokens) {

        Stack<Integer> stack = new Stack<>();

        for ( String s : tokens ) {

            if ( s.equals("+")) {
                int num1 = stack.pop();
                int num2 = stack.pop();
                int res  = num1 + num2;
                stack.push(res); 
            } else if ( s.equals("-")) {
                int num1 = stack.pop();
                int num2 = stack.pop();
                int res  = num2 - num1;
                stack.push(res); 
            } else if ( s.equals("*")) {
                int num1 = stack.pop();
                int num2 = stack.pop();
                int res  = num1 * num2;
                stack.push(res); 
            } else if ( s.equals("/")) {
                int num1 = stack.pop();
                int num2 = stack.pop();
                int res  = num2 / num1;
                stack.push(res); 
            } else {
                int num = Integer.parseInt(s);
                stack.push(num);
            }
        }
        int res = stack.pop();
        return res;   
    }
}
